from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.routes.users import router as user_router
from app.routes.auth import router as auth_router
import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
async def root():
 return {"Welcome to GymNaut!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000, reload=True) 
