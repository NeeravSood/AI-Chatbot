# AI Chatbot with File Upload and Text-to-Speech using Flask, React, and HuggingFace

This project is an AI chatbot built with a Flask backend and a React frontend. It includes functionalities for storing messages, uploading files, and converting text to speech using the HuggingFace API.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Chat interface for sending and receiving messages.
- File upload functionality.
- Text-to-speech conversion using HuggingFace API.
- React frontend served by Flask backend.

## Installation

### Prerequisites
- Python (>=3.6)
- Node.js (>=14.x)
- npm (>=6.x)
- Flask (>=2.x)
- React (>=17.x)

### Backend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-chatbot-flask-react.git
    cd ai-chatbot-flask-react/backend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the `backend` directory and add your HuggingFace API key:
    ```env
    HUGGINGFACE_API_KEY=your_huggingface_api_key_here
    ```

5. Start the Flask server:
    ```sh
    flask run
    ```

### Frontend Setup

1. Navigate to the `frontend` directory:
    ```sh
    cd ../frontend
    ```

2. Install dependencies:
    ```sh
    npm install
    ```

3. Build the React app:
    ```sh
    npm run build
    ```

4. Serve the React app:
    The React app is served by the Flask backend. Ensure the Flask server is running.

## Usage

1. Ensure the Flask server is running.
2. Open your browser and navigate to `http://localhost:5000`.
3. Interact with the chatbot, upload files, and convert text to speech.

### API Endpoints

- **GET /api/messages**: Retrieve all messages.
- **POST /api/messages**: Add a new message.
- **POST /api/upload**: Upload a file.
- **GET /api/tts?text=your_text**: Convert text to speech and return the audio file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature-name
    ```
5. Open a pull request.
IFYKYK
