from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.models import User, Role

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message":"Invalid credentials"}), 401
    role = db.session.get(Role, user.role_id)
    token = create_access_token(identity=str(user.id), additional_claims={"role": role.name if role else "Analyst"})
    return jsonify({"access_token": token, "user": {"id": user.id, "name": user.name, "email": user.email, "role": role.name if role else "Analyst"}})

@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    if not data.get("email") or not data.get("password"):
        return jsonify({"message":"Email and password are required"}), 400
    if User.query.filter_by(email=data["email"].strip().lower()).first():
        return jsonify({"message":"Email already exists"}), 409
    role = Role.query.filter_by(name="Government Officer").first() or Role(name="Government Officer")
    db.session.add(role); db.session.flush()
    user = User(name=data.get("name", "Officer"), email=data["email"].strip().lower(), password_hash=generate_password_hash(data["password"]), role_id=role.id)
    db.session.add(user); db.session.commit()
    return jsonify({"message":"User registered"}), 201

@auth_bp.get("/me")
@jwt_required()
def me():
    user = db.session.get(User, int(get_jwt_identity()))
    role = db.session.get(Role, user.role_id) if user else None
    return jsonify({"id": user.id, "name": user.name, "email": user.email, "role": role.name if role else None}) if user else ({"message":"Not found"}, 404)
