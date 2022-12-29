from ..fields import UserFields
from ..common import BaseModel

class User(BaseModel):
    name: str = UserFields.name
    email: str = UserFields.email
    password: str = UserFields.password
    user_id: str = UserFields.user_id