from datetime import datetime
from sqlalchemy import JSON
from app import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LandParcel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    land_id = db.Column(db.String(40), unique=True, nullable=False)
    survey_number = db.Column(db.String(80))
    district = db.Column(db.String(80), default="Bengaluru Urban")
    taluk = db.Column(db.String(80))
    hobli = db.Column(db.String(80))
    village = db.Column(db.String(120))
    panchayat = db.Column(db.String(120))
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    area_acres = db.Column(db.Float, nullable=False)
    classification = db.Column(db.String(60), nullable=False)
    ownership_category = db.Column(db.String(80))
    utilization_status = db.Column(db.String(80))
    source = db.Column(db.String(255))
    verification_status = db.Column(db.String(30), default="unverified")
    geometry = db.Column(JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SoilObservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    land_id = db.Column(db.Integer, db.ForeignKey("land_parcel.id"), nullable=False)
    ph = db.Column(db.Float)
    moisture = db.Column(db.Float)
    soil_type = db.Column(db.String(80))
    nitrogen = db.Column(db.Float)
    phosphorus = db.Column(db.Float)
    potassium = db.Column(db.Float)
    organic_carbon = db.Column(db.Float)
    source = db.Column(db.String(255))
    is_estimated = db.Column(db.Boolean, default=True)
    observed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    duration_days = db.Column(db.Integer)

class MarketPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey("crop.id"), nullable=False)
    market = db.Column(db.String(120))
    price_per_quintal = db.Column(db.Float)
    observed_at = db.Column(db.DateTime)
    source = db.Column(db.String(255))

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    action = db.Column(db.String(120), nullable=False)
    entity_type = db.Column(db.String(80))
    entity_id = db.Column(db.String(80))
    details = db.Column(JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
