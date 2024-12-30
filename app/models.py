from . import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    status=db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, email, status, created_at, updated_at):
        self.name = name
        self.email = email
        self.status=status
        self.created_at = created_at
        self.updated_at = updated_at