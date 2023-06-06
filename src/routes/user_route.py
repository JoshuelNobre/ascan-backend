from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm.session import Session
from repositories.user_repository import UserRepository
from database.config import get_db
from schemas.user_schema import User


router = APIRouter()


@router.post('/user')
def create(
    user: User,
    db: Session = Depends(get_db)
    ):
    found_user = UserRepository(db).search_by_username(user.username)

    if found_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Username already exists')
    user_created = UserRepository(db).create(user)
    return user_created


@router.get('/users', response_model=List[User])
def list(
    db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users


# @router.delete('/user/{id}')
# def delete(id: int,
    
#            db: Session = Depends(get_db)
#            ):
#     UserRepository(db).remove(id)
#     return {'msg': 'Deleted user sucessfully '}


# @router.get('/user/me', response_model=SimpleUser)
# def get_me(current_user: User = Depends(auth_utils.get_user_logged_in)):
#     return current_user


# @router.put('/user/me')
# def update_me(
#         user: UserEdit,
#         current_user: User = Depends(
#             auth_utils.get_user_logged_in),
#         db: Session = Depends(get_db)):
#     UserRepository(db).edit(current_user.id, user)
#     return {"msg": "user updated"}


# @router.put('/user/{id}')
# def update(
#     id: int,
#     user: User,
#     db: Session = Depends(get_db)
# ):
#     UserRepository(db).edit(id, user)
#     user.id = id
#     return user