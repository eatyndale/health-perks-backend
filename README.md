# Health Perks Backend API

A FastAPI-based backend service for the Health Perks application, providing authentication and chat functionality.

## Features

- User authentication (login/register)
- Chat session management
- AI-powered chat responses
- EFT statement generation
- Reminder phrase generation

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
# The database will be automatically created when you first run the application
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- POST `/api/auth/register` - Register a new user
- POST `/api/auth/login` - Login and get access token

### Chat
- GET `/api/chat/history` - Get user's chat history
- POST `/api/chat/sessions` - Create a new chat session
- POST `/api/chat/respond` - Generate AI response
- POST `/api/chat/statements` - Generate EFT setup statements
- POST `/api/chat/phrases` - Generate reminder phrases

## Security

- JWT-based authentication
- Password hashing with bcrypt
- CORS middleware enabled
- SQLAlchemy for database operations

## Development

The project structure follows a modular design:
```
app/
├── main.py              # Entry point
├── routers/            # API endpoints
├── models/             # Database models
├── schemas/            # Pydantic models
├── services/           # Business logic
└── db/                 # Database configuration
``` 