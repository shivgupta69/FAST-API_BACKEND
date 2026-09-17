# AI Chat-BOT 🤖

A simple AI chatbot backend built with **FastAPI** and the **OpenAI API**.

The backend provides a chat endpoint that accepts a text message and returns an AI-generated response. It also keeps the conversation history in memory and provides an endpoint to clear that history.

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- OpenAI API

## 📁 Files

```text
AI_Chat-BOT/
├── chatbot.py
├── requirements.txt
└── README.md
```

## 🚀 Setup

Clone the repository and move into the chatbot folder:

```bash
git clone https://github.com/shivgupta69/FAST-API_BACKEND.git
cd FAST-API_BACKEND/AI_Chat-BOT
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 OpenAI API Key

The application uses the OpenAI API, so set your API key before starting the server.

### macOS / Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Do not add your API key to the source code or commit it to GitHub.

## ▶️ Run the Server

Start the FastAPI application with:

```bash
uvicorn chatbot:app --reload
```

The server will run at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can test the endpoints directly from the browser.

## 🔗 Endpoints

### `POST /api/chat`

Send a chat message as plain text.

Example using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/api/chat"   -H "Content-Type: text/plain"   -d "Hello, I need help with the chatting service."
```

The endpoint returns the AI response as plain text.

### `DELETE /api`

Clears the current in-memory conversation history.

```bash
curl -X DELETE "http://127.0.0.1:8000/api"
```

## ⚙️ Model

The application uses `gpt-4o-mini` by default.

You can change the model using the `OPENAI_MODEL` environment variable:

```bash
export OPENAI_MODEL="your_model_name"
```

## 👨‍💻 Author

**Shiv Gupta**

GitHub: https://github.com/shivgupta69
