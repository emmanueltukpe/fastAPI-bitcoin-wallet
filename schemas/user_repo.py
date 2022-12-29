from models import *
from exceptions import *
from config.db import user_collection
from utils import get_uuid, get_hashed_password

__all__ = ("UserRepository",)

class UserRepository:
    @staticmethod
    def signup(create: User) -> UserRead:
        user = create.dict()
        user["_id"] = get_uuid()
        user["password"] = get_hashed_password(create.password)
        is_signed_up = user_collection.find_one({"email": create.email})
        if is_signed_up is not None:
            raise PersonAlreadyExistsException
        users = user_collection.insert_one(create)
        assert users.acknowledged
        return user_collection.find_one({"_id": users.inserted_id})