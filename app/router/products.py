from typing import List
from fastapi import APIRouter,Form,UploadFile,File


router = APIRouter(
    prefix='/products',
    tags=['product']
)

@router.post("")
async def post_products(
    name:str = Form(),
    descreption: str | None = Form(None),
    price:float = Form(),
    images:List[UploadFile] = File()

):
    return {
        "responce":name
    }