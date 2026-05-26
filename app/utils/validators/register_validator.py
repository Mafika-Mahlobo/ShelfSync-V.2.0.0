import re
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator, model_validator

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator('name')
    @classmethod
    def normalize_name(cls, value):
        return value.strip().lower()

    @field_validator('email')
    @classmethod
    def normalize_email(cls, value):
        return value.strip().lower()

    @field_validator('password')
    @classmethod
    def validate_password(cls, value):

        if len(value) < 8:
            raise ValueError('Password must not be less than 8 characters.')
        
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase character.')
        
        if not re.search(r'[0-9]', value):
            raise ValueError('Password must contain at least number.')
        
        if not re.search(r'[!@#$%^&*]', value):
            raise ValueError('Password must contain at least one special character.')
        
        return value
    

    @model_validator(mode='after')
    def password_confirm(self):
        
        if not self.password == self.confirm_password:
            raise ValueError('Passwords do not match')
        
        return self
    
class LibrarySchema(BaseModel):
    name: str
    description: Optional[str] = None
    location_address: str
    latitude: float
    longitude: float

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):

        if len(value) < 5:
            raise ValueError('Invalid library name.')
        
        return value.strip().lower()
    
    