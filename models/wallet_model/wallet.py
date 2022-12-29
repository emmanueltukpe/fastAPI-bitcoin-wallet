from pydantic import BaseModel

class Wallet(BaseModel):
    user_id: str 
    naira_balance: int
    bitcoin_balance: int
    account_name: str
    account_number: str