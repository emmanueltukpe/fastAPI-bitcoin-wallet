from pydantic import Field

_string = dict(min_length=1)
"""Common attributes for all String fields"""

class UserFields:
    name = Field(
        description="Full name of this person",
        example="John Smith",
        max_length=100
        # **_string
    )
    email= Field(
        description="Email address of this person",
        example="owufestigies@gmail.com",
        regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        **_string
    )
    password= Field(
        description="Password of this person",
        # min_length=8,
        **_string
    )
    user_id = Field(
        description="Unique identifier of this person in the database",
        # min_length=36,
        max_length=36
    )

class WalletFields:
    user_id: int = Field(..., ge=1)
    account_name: str = Field(..., max_length=100)
    account_number: str = Field(..., max_length=10)
    account_balance: float = Field(..., ge=0)

class Transaction:
    sender_account_number: str = Field(..., max_length=100)
    recipient_account_number: str = Field(..., max_length=100)
    amount: float = Field(..., ge=0)
    transaction_type: str = Field(..., max_length=100)
    
# Sign up - create
# Login - get one
# Create Account - create
# Start Session - get one 
# Withdrawal - update
# Transfer - update
# Fund - update
# Convert from BTC to N - update
# Convert from  N to BTC - update
