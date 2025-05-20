# PyMicro Project

This repository contains two independent Flask microservices: **dashboard** and **login**. Each microservice is self-contained with its own environment, application logic, UI templates, `requirements.txt`, and `Dockerfile` for containerization.

## Project Structure

```
PyMicro/
├── dashboard/
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       └── ... (dashboard HTML templates)
└── login/
   ├── app.py
   ├── .env
   ├── requirements.txt
   ├── Dockerfile
   └── templates/
      └── ... (login HTML templates)
```

## Microservices

### 1. Dashboard Service

- **Location:** `dashboard/`
- **Entry Point:** `app.py`
- **Environment Config:** `.env`
- **Dependencies:** `requirements.txt`
- **Dockerfile:** For building the dashboard image
- **Templates:** UI files in `dashboard/templates/`

### 2. Login Service

- **Location:** `login/`
- **Entry Point:** `app.py`
- **Environment Config:** `.env`
- **Dependencies:** `requirements.txt`
- **Dockerfile:** For building the login image
- **Templates:** UI files in `login/templates/`

## Setup Instructions

1. **Navigate** to the desired microservice directory (`dashboard` or `login`).
2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** in the `.env` file.
   Example `.env` format:

   ```env
   MONGO_CONN_STR=mongodb://localhost:27017/
   LOGIN_PORT=5000
   LOGIN_IP=localhost
   DASHBOARD_PORT=5001
   DASHBOARD_IP=localhost
   SECRET_KEY="login_secret"
   ```

5. **Run the service**:

   ```bash
   python app.py
   ```

## Notes

- Each microservice runs independently.
- UI templates are stored in their respective `templates/` folders.
- Environment variables, dependencies, and Dockerfiles are managed separately for each service.

## Docker Build
g
### Build Login image

```bash
cd login
docker build . -t login:latest
```

### Build Dashboard image

```bash
cd dashboard
docker build . -t dashboard:latest
```

## Docker Run

### Login Run

```bash
docker run --name login -e MONGO_CONN_STR=mongodb://3.3.3.101:30017 -e LOGIN_PORT=5000 -e LOGIN_IP=localhost -e DASHBOARD_PORT=5001 -e DASHBOARD_IP=localhost -e SECRET_KEY="login_secret" -p 5000:5000 -d login:latest
```

### Dashboard Run

```bash
docker run --name dashboard -e MONGO_CONN_STR=mongodb://3.3.3.101:30017 -e LOGIN_PORT=5000 -e LOGIN_IP=3.3.3.101 -e DASHBOARD_PORT=5001 -e DASHBOARD_IP=3.3.3.101 -e SECRET_KEY="login_secret" -p 5001:5001 -d dashboard:latest
```
