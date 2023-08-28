"""Module providing User Repository Class"""

from src.database.sqlalchemy import db
from src.utils import bcrypt
from ..models.user import User, UserSchema


class UsersRepository:
    """User repository methods"""

    def find_by_username(self, username, dump=True) -> User | None:
        """Get all users method"""
        user = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one_or_none()

        if not dump:
            return user

        schema = UserSchema()

        return schema.dump(user) if user else None

    def find_by_id(self, user_id, dump=False) -> User | None:
        """Get all users method"""
        user = db.session.execute(
            db.select(User).filter_by(id=user_id)
        ).scalar_one_or_none()

        if not dump:
            return user

        schema = UserSchema()

        return schema.dump(user) if user else None

    def find_all(self) -> list[User]:
        """Get all users method"""

        users = db.session.execute(db.select(User)).scalars()

        schema = UserSchema(many=True)

        return schema.dump(users)

    def create(self, email, username, password) -> User:
        """Create user method"""

        user = User(
            username=username,
            email=email,
            password=bcrypt.generate_password_hash(password).decode("utf-8"),
        )

        db.session.add(user)
        db.session.commit()

        schema = UserSchema()

        return schema.dump(user)

    def save(self, user) -> User:
        """Save user method"""

        print(user.email)
        db.session.commit()
        print(user.email)

        schema = UserSchema()

        return schema.dump(user)

    def delete(self, user_id):
        """Delete user method"""

        user = db.session.execute(
            db.select(User).filter_by(id=user_id)
        ).scalar_one_or_none()

        if not user:
            return

        db.session.delete(user)
        db.session.commit()
