# PyMicro Project

This repository contains two independent Flask microservices: **dashboard** and **login**. Each microservice is self-contained with its own environment, application logic, and UI templates.

## Project Structure

```
PyMicro/
├── dashboard/
│   ├── app.py
│   ├── .env
│   └── templates/
│       └── ... (dashboard HTML templates)
└── login/
	├── app.py
	├── .env
	└── templates/
		└── ... (login HTML templates)
```

## Microservices

### 1. Dashboard Service

- **Location:** `dashboard/`
- **Entry Point:** `app.py`
- **Environment Config:** `.env`
- **Templates:** UI files in `dashboard/templates/`

### 2. Login Service

- **Location:** `login/`
- **Entry Point:** `app.py`
- **Environment Config:** `.env`
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
- Environment variables are managed separately for each service.
