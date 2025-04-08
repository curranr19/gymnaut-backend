from bson import ObjectId
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class Profile(BaseModel):
    profile_id: Optional[str] = None
    first_name: str
    last_name: str
    dob: date
    address: str
    city: str
    mobile: str
    current_weight: float
    target_weight: float
    fitness_ability: str