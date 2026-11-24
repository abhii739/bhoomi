# BhoomiAI

AI-powered land intelligence and sustainable agriculture platform for Bengaluru Urban.

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
flask --app wsgi:app run --port 5000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

See `docs/architecture.md`, `docs/api.md`, and `docker-compose.yml` for setup details.
