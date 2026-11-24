import os
from app import db
from app.models.models import Role, User
from werkzeug.security import generate_password_hash

def seed():
    if not Role.query.first():
        names=["Administrator","Government Officer","Agricultural Officer","Analyst"]
        for name in names: db.session.add(Role(name=name))
        db.session.commit()
    if not User.query.filter_by(email="officer@bhoomi.local").first():
        role=Role.query.filter_by(name="Government Officer").first()
        db.session.add(User(name="Demo Officer",email="officer@bhoomi.local",password_hash=generate_password_hash("bhoomi123"),role_id=role.id))
        db.session.commit()
