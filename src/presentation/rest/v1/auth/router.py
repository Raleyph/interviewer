from fastapi import APIRouter, Request

router = APIRouter(prefix="/auth")


@router.get("/login")
async def login(request: Request):
    pass


@router.get("/callback")
async def callback(request: Request):
    pass
