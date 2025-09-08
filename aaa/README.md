# RADIUS Admin (Vue 3 + Bootstrap + Vite 7) + Flask Backend

## Overview
This repository contains a simple admin UI (Vue 3 + Vite 7 + Bootstrap 5) that talks to a Flask backend.
The backend exposes basic CRUD endpoints for RADIUS-related tables (`radcheck`, `radgroupcheck`, `nas`).

## Quick start (development)

### Backend (Python)
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate   # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Copy `backend/.env.example` to `.env` (or set environment variables) and update DB credentials if needed.
4. Run the backend:
   ```bash
   cd backend
   python run.py
   ```
   The Flask server will start on `http://127.0.0.1:5000` by default.

### Frontend (Node / npm)
1. Install Node.js (recommended Node 20.19+ or 22.12+ for Vite 7).
2. Install dependencies and run dev server:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
3. By default the frontend dev server runs on port `5173`. The frontend reads `VITE_API_BASE_URL` from `frontend/.env.example` (copy to `.env` and change if needed).

## Notes & Recommendations
- The project defaults keep RADIUS passwords in `radcheck.value` as cleartext (common for RADIUS setups). If you prefer not to store cleartext, adapt the authentication flow accordingly.
- CORS is enabled for development in `backend/app/__init__.py`. For production, restrict allowed origins.
- Secrets in `config.py` are defaults for development only — **change them** for production and **do not commit secret values**.

## What I changed
- Made `backend/app/config.py` environment-aware (reads DB credentials from env vars).
- Added `backend/.env.example` with sample env variables.
- Added this `README.md` with quick start instructions.
- Added `.gitignore` (see below).

## .gitignore (suggested)
- `node_modules/`
- `venv/`
- `*.pyc`
- `.env`
