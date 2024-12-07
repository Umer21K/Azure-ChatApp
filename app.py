# from gevent import monkey
# monkey.patch_all()

from flask_socketio import SocketIO, join_room, leave_room, emit
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from blob_storage import *
from database import *
from dotenv import load_dotenv

import logging
load_dotenv()
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
app = Flask(__name__, static_folder='static', template_folder='static')
app.logger.setLevel(logging.INFO)
socketio = SocketIO(app, async_mode="eventlet",cors_allowed_origins='*')
CORS(app)  # Enable CORS for frontend-backend communication

def handle_error(message, error, status_code=500):
    app.logger.error(f"{message}: {error}")
    return jsonify({'success': False, 'message': 'An unexpected error occurred. Please try again later.'}), status_code

@app.route('/')
@app.route('/<path:path>')
def serve_angular(path=None):
    app.logger.info(f"Serving Angular app for path: {path}")
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/add_user', methods=['POST'])
async def add_user_api():
    try:
        data = request.json
        app.logger.info(f"Add user API called with data: {data}")
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')

        user_info = await add_user(name, password, email)
        
        if user_info:
            app.logger.info(f"User {name} added successfully with ID {user_info['id']}")
            return jsonify({'success': True, 'userid': user_info['id'], 'username': user_info['name']}), 201
        else:
            app.logger.warning(f"User already exists: {email}")
            return jsonify({'success': False, 'message': 'User already exists with that name or email'}), 200
    except Exception as e:
        app.logger.error(f"Error adding user: {e}")
        return handle_error("Error adding user", e)

@app.route('/api/validate_user', methods=['POST'])
async def validate_user_api():
    try:
        data = request.json
        app.logger.info(f"Validate user API called with data: {data}")
        email = data.get('email')
        password = data.get('password')
        
        user_info = await validate_user(password, email)
        
        if user_info:
            app.logger.info(f"User {email} validated successfully")
            return jsonify({'success': True, 'userid': user_info['userid'], 'username': user_info['username']}), 200
        else:
            app.logger.warning(f"Invalid credentials for user {email}")
            return jsonify({'success': False,'message': 'Invalid credentials'}), 200
    except Exception as e:
        app.logger.error(f"Error validating user: {e}")
        return handle_error("Error validating user", e)

@app.route('/api/get_other_users/<userid>', methods=['GET'])
async def get_other_users_api(userid):
    try:
        users = await get_other_users(userid)

        app.logger.info(f"Fetching other users for user ID: {userid}")
        # Return success response
        app.logger.info(f"Found {len(users)} other users for user ID: {userid}")
        return jsonify({'success': True, 'data': users}), 200
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error fetching other users for user ID {userid}: {e}")
        return handle_error("Error getting users", e)

@app.route('/api/get_rooms/<userid>', methods=['GET'])
async def get_rooms_api(userid):
    try:
        app.logger.info(f"Fetching rooms for user ID: {userid}")
        # Fetch rooms for the given user ID
        rooms = await get_rooms(userid)
        app.logger.info(f"Found {len(rooms)} rooms for user ID: {userid}")

        # Return success response with room data
        return jsonify({'success': True, 'data': rooms}), 200
    except Exception as e:
        app.logger.error(f"Error fetching rooms for user ID {userid}: {e}")
        # Return a generic error message
        return handle_error("Error getting rooms", e)


@app.route('/api/get_messages/<roomid>', methods=['GET'])
async def get_messages_api(roomid):
    try:
        app.logger.info(f"Fetching messages for room ID: {roomid}")
        messages = await get_messages(roomid)
        app.logger.info(f"Found {len(messages)} messages for room ID: {roomid}")

        return jsonify({'success': True, 'data': messages}), 200
    except Exception as e:
        app.logger.error(f"Error fetching messages for room ID {roomid}: {e}")
        # Return a generic error message
        return handle_error("Error getting messages", e)

@app.route('/api/create_room', methods=['POST'])
async def create_room_api():
    try:
        data = request.json
        app.logger.info(f"Create room API called with data: {data}")
        User1 = data['User1']
        User2 = data['User2']

        await create_room(User1, User2)
        app.logger.info(f"Room created successfully between {User1} and {User2}")
        return jsonify({'success': True, 'message': 'Chat created successfuly'}),  201
    except Exception as e:
        app.logger.error(f"Error creating room: {e}")
        # Return a generic error message
        return handle_error("Error creating room", e)

@app.route('/api/send_message', methods=['POST'])
async def send_message_api():
    try:
        data = request.json
        app.logger.info(f"Send message API called with data: {data}")
        message = data['message']
        await send_message(message)
        app.logger.info(f"Message sent successfully: {message}")
        return jsonify({'success': True, 'message': 'Message sent successfuly'}),  201
    except Exception as e:
        app.logger.error(f"Error sending message: {e}")
        # Return a generic error message
        return handle_error("Error sending message", e)

@app.route('/api/send_message_nimbus', methods=['POST'])
async def send_message_nimbus_api():
    try:
        data = request.json
        app.logger.info(f"Send message to Nimbus API called with data: {data}")
        message = data['message']
        app.logger.info(f"Message to Nimbus API sent successfuly")
        await chat_with_nimbus(message)
        return jsonify({'success': True, 'message': 'Message sent successfuly'}),  201
    except Exception as e:
        app.logger.error(f"Error sending message to nimbus: {e}")
        # Return a generic error message
        return handle_error("Error sending message to nimbus", e)

@app.route('/api/send_file', methods=['POST'])
async def send_file_api():
    try:
        room_id = request.form.get('roomid')  # Get the room ID from the form
        file = request.files['file']  # Get the uploaded file
        file_name = file.filename  # Extract the file name
        file_data = file.read()  # Read the file content

        app.logger.info(f"Sending file to room {room_id}, {file_name}, {file_data}")
        # Call the Azure function to upload the file
        await send_file(room_id, file_data, file_name)
        app.logger.info(f"Sending file to room successfuly")

        return jsonify({'success': True, 'message': 'Image sent successfully'}), 201
    except Exception as e:
        app.logger.error(f"Error sending file: {e}")
        # Return a generic error message
        return handle_error("Error sending file", e)

@app.route('/api/get_files/<room_id>', methods=['GET'])
async def get_files_api(room_id):
    try:
        app.logger.info(f"Getting files from room {room_id}")
        # Call the Azure function to get files
        files = await get_files(room_id)
        app.logger.info(f"Success getting files from room {room_id}")
        return jsonify({'success': True, 'files': files}), 200
    except Exception as e:
        app.logger.error(f"Error getting files: {e}")
        # Return a generic error message
        return handle_error("Error getting file", e)

@socketio.on('message')
def handle_message(data):
    message = data['message']
    room = data['room']
    sender_name = data['senderName']

    # Emit the message back to all clients in the room
    emit('message', {'message': message, 'room': room, 'senderName': sender_name }, to=room)

@socketio.on('join_room')
def handle_join_room(data):
    room = data['room']
    join_room(room)

@socketio.on('leave_room')
def handle_leave_room(data):
    room = data['room']
    leave_room(room)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000))) 