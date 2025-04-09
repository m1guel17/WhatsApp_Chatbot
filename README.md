<div align="center">
  <a>
    <img src="https://github.com/user-attachments/assets/141434ef-3204-4cdf-9e1b-c3eae4e25713" style="width:15%; height:auto;">
  </a>
  <h1 align="center">WhatsApp Chatbot</h1>

  <p align="center">
    An awesome Chatbot module template to integrate into your projects!
    <br />
    <a href="https://github.com/m1guel17/WhatsApp_Chatbot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/m1guel17/WhatsApp_Chatbot">View Demo</a>
    &middot;
    <a href="https://github.com/m1guel17/WhatsApp_Chatbot">Report Bug</a>
    &middot;
    <a href="https://github.com/m1guel17/WhatsApp_Chatbot">Request Feature</a>
  </p>
</div>

Made by [m1guel17](https://github.com/m1guel17)
<!--
    <img src="https://github.com/user-attachments/assets/ff5b782f-778f-427a-9b76-6742eb4d7836" style="width:25%; height:auto;">
<img src="https://github.com/user-attachments/assets/0c1c6f44-ee0d-4dfd-a9f5-a0613f802231" style="width:100%; height:auto;">
<img src="https://github.com/user-attachments/assets/79c497be-7242-4bcc-a740-e620d52d8c61" style="width:10%; height:auto;">
<img src="https://github.com/user-attachments/assets/1aa1eb45-9437-4600-9df0-03d095a290b5" style="width:10%; height:auto;">
-->
A Django-based WhatsApp chatbot that integrates with the Meta (Facebook) WhatsApp Business API. This chatbot handles incoming WhatsApp messages via webhooks, processes them using a built-in chatflow engine, and responds according to a user’s position in the flow. It also can manage each user’s state throughout a conversation.
<br>

# Features
- **Integration with Meta WhatsApp API**: Sends and receives messages via the official WhatsApp Business API.
- **Chatflow Engine**: Manages conversation flows (states and transitions) for each user.
- **Django ORM for State Management**: Store user-specific states in the database to track progress in real time.

# Configuration
1. Environment Variables
Create a .env file or use your system’s environment variables to specify:
```bash
WHATSAPP_VERIFY_TOKEN=your_verify_token
WHATSAPP_BUSINESS_ACCESS_TOKEN=your_meta_api_access_token
DJANGO_SECRET_KEY=your_django_secret_key
DEBUG=True
```
Replace the placeholders with your actual credentials

# Chatflow Engine Overview
The chatflow engine keeps track of each user’s progression in a conversation. Below is a typical flow:
1. Identify the User: Use the user’s WhatsApp phone number to look up their current state in the database.

2. Check Current State: Retrieve the user’s current step in the flow (e.g., "WELCOME", "GATHERING_INFO", "CONFIRMATION", etc.).

3. Transition Logic: Based on the incoming message (text, media, etc.) and the current state, the flow manager transitions the user to the appropriate next step.

4. Generate Response: The chatflow engine returns a response string (or multiple messages), which the view sends back to WhatsApp via the Meta API.

5. Store the Updated State: The engine will save user input and the new state to the database.

## Roadmap
- [x] Initial Setup & Webhook Validation
    - [x] Set up a Django project and create a chatbot app
    - [x] Implement `/webhook` endpoint to validate domain with Meta
    - [x] Deploy to a Render hosting platform for testing
    - [x] Successfully receive and print test payloads for debugging

- [ ] Core Chatbot Features
  - [ ] **Message Parsing & Handling**  
    - [ ] Parse incoming WhatsApp payloads (e.g., text, media)  
    - [ ] Store or log messages for analytics/tracking  
  - [ ] **Response Logic**  
    - [ ] Create a simple “If user says X, respond with Y” logic  
    - [ ] (Optional) Integrate NLP or advanced AI to generate dynamic responses  
  - [ ] **Message Sending**  
    - [ ] Use the WhatsApp Business API to send text messages  
    - [ ] Extend functionality for media and template messages  

- [ ] Additional Templates & Examples
  - [ ] Provide reusable code snippets for different message types (text, media, location)
  - [ ] Demonstrate how to handle user state or multi-step conversation flows

- [ ] Deployment & Scaling
  - [ ] Deploy to a secure hosting platform (e.g., AWS, DigitalOcean, Heroku) with HTTPS
  - [ ] Configure environment variables for tokens and secrets

## Contact
[LinkedIn](https://www.linkedin.com/in/miguel-esteban-flores-sierra/)
