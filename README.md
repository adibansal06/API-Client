
# API-Client

A Python-based API client that interacts with a Log Portal to authenticate users, retrieve live logs, and control devices through REST APIs.

## 📌 Project Overview

This project was developed as part of an API reverse-engineering assignment. The objective was to understand how a web dashboard communicates with its backend APIs and build a command-line client that performs similar operations.

The API endpoints were discovered by inspecting network requests through browser Developer Tools.

## ✨ Features

- User authentication using username and password
- Secure API requests using Bearer token authentication
- Fetching and displaying live system logs
- Retrieving available devices and their current states
- Toggling authorized devices
- Clear error handling for:
  - Invalid credentials
  - Invalid or expired authentication tokens
  - Network failures
- Modular Python code structure

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – HTTP API communication
- **REST APIs**
- **JSON**
- **Browser Developer Tools**
- **HTTPS**

## 📂 Project Structure

```text
API-Client/
│
├── api_client.py       # API request and response handling
├── log_stream.py       # Continuous live log streaming
├── main.py             # Application entry point and user interaction
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies (if available)
```

## 🔍 API Discovery Process

The API endpoints were identified by observing network requests made by the web dashboard.

### 1. Login API

- **Method:** `POST`
- **Endpoint:** `/api/login`
- **Purpose:** Authenticates the user and returns an authentication token.

### 2. Logs API

- **Method:** `GET`
- **Endpoint:** `/api/logs`
- **Purpose:** Retrieves system logs from the portal.
- **Authentication:** Bearer token required.

### 3. Controls API

- **Method:** `GET`
- **Endpoint:** `/api/controls`
- **Purpose:** Retrieves the available devices, their states, and control permissions.
- **Authentication:** Bearer token required.

### 4. Toggle API

- **Method:** `POST`
- **Endpoint:** `/api/controls/{device_id}/toggle`
- **Purpose:** Changes the state of a specific authorized device.
- **Authentication:** Bearer token required.

> **Note:** The base URL is configured by the user when running the application.

## 🔐 Authentication

After successful login, the server provides an authentication token.

This token must be included in subsequent API requests using the `Authorization` header:

```http
Authorization: Bearer <token>
```

The server uses this token to verify whether the request is authenticated and authorized.

Requests without a valid token may be rejected with an authentication or authorization error.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd API-Client
```

### 2. Install Dependencies

Make sure Python is installed on your system.

Install the required dependency:

```bash
pip install requests
```

If a `requirements.txt` file is available, use:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python main.py
```

The application will ask for:

- Portal URL
- Username
- Password

Follow the instructions displayed in the terminal.

## 🔄 Application Workflow

```text
Start Application
       │
       ▼
Enter Portal URL and Credentials
       │
       ▼
Authenticate User
       │
       ▼
Receive Bearer Token
       │
       ▼
Read Live Logs / View Controls
       │
       ▼
Toggle Authorized Device
       │
       ▼
Display Result
```

## 🧪 Testing

The application was tested for the following scenarios:

- Successful user login
- Retrieval of system logs
- Continuous log streaming
- Retrieval of device controls
- Toggling an authorized device
- Handling incorrect credentials
- Handling invalid authentication tokens
- Handling network failures

## 📚 Key Concepts Learned

- HTTP request methods (`GET` and `POST`)
- API endpoints and URL paths
- Request headers and authentication
- Bearer token authentication
- JSON request and response formats
- HTTP status codes
- API discovery using browser Developer Tools
- Modular programming in Python
- Error handling in API clients

## 👨‍💻 Author

**Aditya Bansal**

## 📄 License

This project was developed for educational and assignment purposes.
