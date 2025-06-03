from fastapi import APIRouter
from .endpoints.categorias import router as categoria_router
from .endpoints.produtos import router as produto_router

router = APIRouter()

router.include_router(categoria_router)
router.include_router(produto_router)