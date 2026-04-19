import re
from pydantic import BaseModel, EmailStr, field_validator

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):

        if len(v) < 8:
            raise ValueError('Password must not be less than 8 characters.')
        
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase character.')
        
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least number')
        
        if not re.search(r'[!@#$%^&*]', v):
            raise ValueError('Password must contain at least one special character.')
        
        return v