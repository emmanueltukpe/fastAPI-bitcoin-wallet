from datetime import datetime
from typing import Optional, List

# # Installed # #
import pydantic

# # Package # #
from .user_create import User
from ..fields import UserFields

__all__ = ("UserRead",)


class UserRead(User):
    """Body of Person GET and POST responses"""
    user_id: str = UserFields.user_id
    name: str = UserFields.name
    email: str = UserFields.email
    password: str = UserFields.password

    @pydantic.root_validator(pre=True)
    def _set_user_id(cls, data):
        """Swap the field _id to person_id (this could be done with field alias, by setting the field as "_id"
        and the alias as "person_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["user_id"] = document_id
        return data

    class Config(User.Config):
        extra = pydantic.Extra.ignore 