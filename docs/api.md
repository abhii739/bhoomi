# API contract

## Authentication
- `POST /api/auth/login`
- `POST /api/auth/register`
- `GET /api/auth/me`

## Domain APIs
- `GET /api/lands`
- `GET /api/lands/<land_id>`
- `GET /api/soil/<land_id>?lat=&lon=`
- `GET /api/crops/recommendations?land_id=`
- `GET /api/market/prices`
- `GET /api/market/employment?area_acres=`
- `POST /api/reports/excel`
- `POST /api/reports/pdf`

Development login: `officer@bhoomi.local` / `bhoomi123`
