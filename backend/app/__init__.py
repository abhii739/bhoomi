from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", "sqlite:///bhoomi.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY=os.getenv("SECRET_KEY", "development-secret"),
        JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY", "development-jwt-secret"),
    )
    CORS(app, origins=os.getenv("CORS_ORIGINS", "http://localhost:5173").split(","))
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from app.auth.routes import auth_bp
    from app.land.routes import land_bp
    from app.soil.routes import soil_bp
    from app.crops.routes import crops_bp
    from app.market.routes import market_bp
    from app.reports.routes import reports_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(land_bp, url_prefix="/api/lands")
    app.register_blueprint(soil_bp, url_prefix="/api/soil")
    app.register_blueprint(crops_bp, url_prefix="/api/crops")
    app.register_blueprint(market_bp, url_prefix="/api/market")
    app.register_blueprint(reports_bp, url_prefix="/api/reports")

    with app.app_context():
        db.create_all()
    return app
