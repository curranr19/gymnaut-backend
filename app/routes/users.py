from fastapi import APIRouter, HTTPException
from app.models.users import User
from app.db.database import db, users
from passlib.context import CryptContext
from datetime import datetime, timezone

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register")
async def register_user(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")


    hashed_password = pwd_context.hash(user.password)

   
    user_dict = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,  
        "created_at": datetime.now(timezone.utc)
    }

    
    result = await db.users.insert_one(user_dict)
    user_id = str(result.inserted_id)

    empty_profile = {
        "profile_id": str(user_id),
        "first_name": "",
        "last_name": "",
        "dob": None,
        "address": "",
        "city": "",
        "mobile": "",
        "current_weight": 0.0,
        "target_weight": 0.0,
        "fitness_ability": ""
    }
    return {"message": "User registered successfully", "id": str(result.inserted_id)}


