from pydantic import BaseModel

class Transaction(BaseModel):
    sender_account_number: str
    recipient_account_number: str
    transaction_type: str
    amount: int