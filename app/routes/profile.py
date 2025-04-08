from fastapi import APIRouter, HTTPException, Depends
from app.models.profile import Profile
from app.models.users import User
from app.db.database import db, profiles
from bson import ObjectId
from jose import jwt, JWTError
from app.routes.auth import get_current_user
from datetime import datetime

    

router = APIRouter()

@router.post("/")
async def create_profile(profile: Profile, current_user: dict = Depends(get_current_user)):
    profile_id = str(current_user["_id"])

    # Check if the profile already exists
    existing_profile = await profiles.find_one({"profile_id": profile_id})
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists")

    profile_dict = profile.dict()
    profile_dict["profile_id"] = str(current_user["_id"]) #to link profile to current user
    # profile_dict["_id"] = ObjectId()
    profile_dict["dob"] = datetime.combine(profile_dict["dob"], datetime.min.time())

    result = await profiles.insert_one(profile_dict)
    return {"message": "Profile created successfully", "profile_id": str(result.inserted_id)}
   


# Get user profile by user_id (_id)
@router.get("/{profile_id}")
async def get_profile(profile_id: str, current_user: User = Depends(get_current_user)):
    profile = await profiles.find_one({"profile_id": profile_id})
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile["_id"] = str(profile["_id"])  # Convert ObjectId to string
    return profile 