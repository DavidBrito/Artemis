"""Module provinding users models"""

from datetime import datetime
from src.database.sqlalchemy import db, ma


class User(db.Model):
    """SQLAlchemy's DB Model"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class UserSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow's Schema"""

    class Meta:
        """Meta class configuration"""

        model = User

