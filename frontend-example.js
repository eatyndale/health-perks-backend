// Example frontend code for connecting to the Health Perks API
// This can be used with React, Vue, or any other frontend framework

// API base URL
const API_BASE_URL = 'http://localhost:8000/api';

// Authentication functions
async function registerUser(email, password, fullName) {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password,
                full_name: fullName
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Registration error:', error);
        throw error;
    }
}

async function loginUser(email, password) {
    try {
        const formData = new FormData();
        formData.append('username', email);
        formData.append('password', password);

        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        // Store the token in localStorage or a secure storage
        localStorage.setItem('token', data.access_token);
        return data;
    } catch (error) {
        console.error('Login error:', error);
        throw error;
    }
}

// Chat functions
async function getChatHistory() {
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_BASE_URL}/chat/history`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        return await response.json();
    } catch (error) {
        console.error('Error fetching chat history:', error);
        throw error;
    }
}

async function createChatSession(title) {
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_BASE_URL}/chat/sessions`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title })
        });
        return await response.json();
    } catch (error) {
        console.error('Error creating chat session:', error);
        throw error;
    }
}

async function sendMessage(sessionId, message) {
    try {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_BASE_URL}/chat/respond`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message,
                session_id: sessionId
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Error sending message:', error);
        throw error;
    }
}

// Example usage:
/*
// Register a new user
registerUser('user@example.com', 'password123', 'John Doe')
    .then(response => console.log('Registration successful:', response))
    .catch(error => console.error('Registration failed:', error));

// Login
loginUser('user@example.com', 'password123')
    .then(response => console.log('Login successful:', response))
    .catch(error => console.error('Login failed:', error));

// Get chat history
getChatHistory()
    .then(sessions => console.log('Chat history:', sessions))
    .catch(error => console.error('Failed to fetch chat history:', error));

// Create a new chat session
createChatSession('New Session')
    .then(session => console.log('New session created:', session))
    .catch(error => console.error('Failed to create session:', error));

// Send a message
sendMessage(1, 'Hello, how are you?')
    .then(response => console.log('Response received:', response))
    .catch(error => console.error('Failed to send message:', error));
*/ 