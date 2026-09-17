# FAST-API_BACKEND 🚀

A collection of **FastAPI backend projects, APIs, and experiments** built with Python.

This repository contains my practical work with FastAPI, covering backend development, REST APIs, API integration, and other backend concepts.

## ⚡ About FastAPI

FastAPI is a modern and high-performance Python framework for building APIs.

It provides:

- Simple and fast API development
- Request and response handling
- Data validation
- Python type hints
- Automatic API documentation
- Swagger UI
- ReDoc
- Support for asynchronous programming

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- REST APIs
- Pydantic
- Git & GitHub

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivgupta69/FAST-API_BACKEND.git
cd FAST-API_BACKEND
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Go to the required project folder and install its dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the FastAPI Server

Go to the folder containing the FastAPI application.

If the application file is `main.py` and contains:

```python
from fastapi import FastAPI

app = FastAPI()
```

Run the server with:

```bash
uvicorn main:app --reload
```

Here:

```text
main  → Python file (main.py)
app   → FastAPI application object
```

The `--reload` option automatically reloads the server when code changes.

The server will normally run at:

```text
http://127.0.0.1:8000
```

> The command may be different for individual projects depending on their Python filename and FastAPI application object.

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

- View available endpoints
- Send API requests
- Enter parameters
- Send request bodies
- View API responses

### ReDoc

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

## 🔗 Using API Endpoints

Once the server is running, endpoints can be used through:

- Swagger UI
- Postman
- cURL
- Frontend applications
- Other backend services

Example:

```bash
curl http://127.0.0.1:8000/
```

For `POST`, `PUT`, or other endpoints that require data, use the request body or parameters specified by that project's API documentation.

## 📁 Project Structure

More FastAPI projects will be added to this repository over time.

```text
FAST-API_BACKEND/
│
├── Project-1/
│   ├── ...
│   └── requirements.txt
│
├── Project-2/
│   ├── ...
│   └── requirements.txt
│
├── Project-3/
│   ├── ...
│   └── requirements.txt
│
└── README.md
```

Each project can contain its own README with project-specific setup and API usage instructions.

## 🔮 Future Projects

This repository will continue to grow with more FastAPI backend projects covering topics such as:

- REST APIs
- Authentication
- Databases
- AI/LLM APIs
- RAG
- AI Agents
- API integrations
- Backend services

## 👨‍💻 Author

**Shiv Gupta**

GitHub: [@shivgupta69](https://github.com/shivgupta69)
