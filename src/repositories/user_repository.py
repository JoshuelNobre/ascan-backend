from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete, select
from schemas import user_schema
from models import models
# from sqlalchemy import update


class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: user_schema):
        db_user = models.User(
            username=user.username,
            created=user.created
            )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list(self):
        users = self.db.query(models.User).all()
        return users

    # def edit(self, id: int, user: schemasEdit):
    #     updated_stmt = update(models.User).where(models.User.id == id).values(
    #         username=user.username,
    #         name=user.name,
    #         surname=user.surname,
    #         email=user.email,
    #         admin=user.admin
    #     )
    #     self.db.execute(updated_stmt)
    #     self.db.commit()

    # def remove(self, id: int):
    #     delete_stmt = delete(models.User).where(models.User.id == id)
    #     self.db.execute(delete_stmt)
    #     self.db.commit()

    def search_by_username(self, username) -> models.User:
        query = select(models.User).where(models.User.username == username)
        return self.db.execute(query).scalars().first()

    # def search_admin_by_username(self, username) -> models.User:
    #     query = select(
    #         models.User).where(
    #         models.User.username == username,
    #         models.User.admin)
    #     return self.db.execute(query).scalars().first()