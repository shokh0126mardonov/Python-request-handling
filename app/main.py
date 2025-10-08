from fastapi import FastAPI

from .models.products import Product,Image
from .db.database import Base,engine
from .router.products import router as products_router

Base.metadata.create_all(engine)

app = FastAPI(
    title='Shop Api',reload = True
    )

app.include_router(products_router)