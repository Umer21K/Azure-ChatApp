# Azure-Chatapp Batein
![image](https://github.com/user-attachments/assets/782e79ff-3bd6-4ed2-ba36-7ebbfbba1e9a)

## Table of Contents
1. **Project Overview**
2. **Objectives**
3. **Application Design and Architecture**  
   3.1 Architecture Diagram  
   3.2 Azure Services Overview  
4. **Functional Requirements**  
   4.1 User Features  
   4.2 API Integration & Azure Function Details  
   4.3 Cloud Hosting & Database Setup  
   4.4 Storage Integration  
   4.5 Monitoring & Security  
5. **Non-Functional Requirements**  
   5.1 Performance & Scalability  
   5.2 Availability & Security  
   5.3 Cost Optimization  
6. **Implementation Details**  
   6.1 Azure Deployment Steps  
   6.2 Challenges & Solutions  
7. **Azure Services Configuration**  
   7.1 App Service Configuration  
   7.2 Database Setup  
   7.3 Key Vault Security Configuration  
8. **Cost Management & Analysis**  
   8.1 Cost Optimization Strategies  
9. **Conclusion & Key Learnings**  
10. **References**  
11. **Appendices**  

## Project Overview
This project focuses on developing a cloud-based chat application leveraging Microsoft Azure services for real-time communication. Users can chat with one another or interact with a chatbot powered by the Gemini API. Key components include:

- **Frontend**: Built with Angular for instant messaging, chatbot interaction, and user authentication.
- **Backend**: Hosted on Azure App Services for reliability and scalability.
- **Database**: Azure Cosmos DB ensures efficient and secure data management.
- **Security**: Azure Key Vault encrypts sensitive information like passwords and API keys.
- **Cross-Platform Compatibility**: Accessible on multiple operating systems for a broad user base.

Explore the live application here: [Batey Chat App](https://batey-cwerh7duhsh0efdx.eastasia-01.azurewebsites.net)

## Objectives
1. Leverage **Microsoft Azure services** for a scalable and efficient application.
2. Securely manage sensitive data (e.g., passwords, API keys) using **Azure Key Vault**.
3. Enable **real-time chatbot interactions** via the Gemini API.
4. Optimize **cloud hosting costs** while ensuring performance.
5. Implement robust **real-time messaging** capabilities for seamless user-to-user and user-to-bot interactions.
6. Develop **web and mobile prototypes** to expand the user base.
7. Utilize **Azure regions** to ensure high performance and uptime globally.

## Application Design and Architecture
### 3.1 Architecture Diagram
[Include your architecture diagram here]

### 3.2 Azure Services Overview
1. **Azure Cosmos DB**: Provides scalable, low-latency storage for user and chat data.
2. **Azure Key Vault**: Secures user credentials and sensitive keys with robust encryption.
3. **Azure App Service**: Hosts the backend for reliable, scalable operations.
4. **Gemini API**: Powers chatbot interactions with intelligent conversational capabilities.
5. **Microsoft Entra ID**: Enforces role-based access control for development team collaboration.

## Functional Requirements
### 4.1 User Features
- Real-time user-to-user chat.
- Chatbot interactions using Gemini API.

### 4.2 API Integration & Azure Function Details
- Gemini API integration for dynamic chatbot interactions.
- Secure retrieval of credentials via Azure Key Vault APIs.

### 4.3 Cloud Hosting & Database Setup
- Backend hosted on **Azure App Service**.
- Chat logs and user data stored in **Azure Cosmos DB**.

### 4.4 Storage Integration
- **Azure Key Vault** for secure credential storage.

### 4.5 Monitoring & Security
- Performance monitoring via **Azure Monitor** and **Application Insights**.
- Secure access control using **Microsoft Entra ID**.

## Non-Functional Requirements
### 5.1 Performance & Scalability
- Optimized asynchronous functionality for low-latency messaging.
- Scalable architecture using Azure services like **Cosmos DB** and **App Service**.

### 5.2 Availability & Security
- High availability ensured by Azure App Service.
- Data security via **Azure Key Vault**.

### 5.3 Cost Optimization
- Deployed using free and standard Azure tiers.
- Optimized database partitions for usage-based scaling.

## Implementation Details
### 6.1 Azure Deployment Steps
1. Configured Angular frontend and Python backend.
2. Integrated Azure Cosmos DB and Key Vault.
3. Deployed the application using Azure App Service.

### 6.2 Challenges & Solutions
- **Credential Security**: Solved using Azure Key Vault for encrypted storage.
- **Real-Time Communication**: Implemented WebSockets and optimized API calls for instant message delivery.

## Azure Services Configuration
### 7.1 App Service Configuration
- Deployed the backend using Python runtime on Azure App Service.

### 7.2 Database Setup
- Configured Azure Cosmos DB with partitions for scalability.

### 7.3 Key Vault Security Configuration
- Managed sensitive keys and credentials securely.

## Cost Management & Analysis
### 8.1 Cost Optimization Strategies
- Leveraged free and standard tiers for cost efficiency.
- Scaled database usage based on actual demand.

## Conclusion & Key Learnings
This project highlights the potential of **Microsoft Azure** in building secure, scalable, and efficient cloud-based applications. By combining Azure Cosmos DB, Key Vault, and App Service, we achieved robust data management, enhanced security, and seamless deployment. Integrating the Gemini API further showcased AI-driven interactions to enhance user experience. Key takeaways include:

- Effective cost management strategies.
- Secure authentication and data handling.
- Scalable architecture for real-world applications.

## References
1. [Microsoft Azure Documentation](https://learn.microsoft.com/en-us/azure/)
2. [Angular Official Documentation](https://angular.io/docs)

## Appendices
- registration page:
![image](https://github.com/user-attachments/assets/ed0487ed-0d4a-40c4-a879-591717f38500)
- login page:
 ![image](https://github.com/user-attachments/assets/3270b423-cc8d-4212-8544-23645ffa5c86)
 - chatbot:
 ![image](https://github.com/user-attachments/assets/377488be-cabc-4ce6-91b2-3620efb31c07)
- chat page:
 ![image](https://github.com/user-attachments/assets/bd9a3fee-d8e4-4a5c-a72c-c06eb4418750)
- select newchat:
 ![image](https://github.com/user-attachments/assets/683fecb7-2243-4fc2-a512-82659c679c03)
- chat between two user:
 ![image](https://github.com/user-attachments/assets/ab596e95-558d-4870-bc68-bf5912efccfd)



 




