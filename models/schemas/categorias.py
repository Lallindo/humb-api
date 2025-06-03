from pydantic import Field, BaseModel as Base
from typing import List, Optional
from core import QueryMeta

class CategoriaBase(Base):
    descritivo_categoria: Optional[str] = Field(default="", description="Nome da categoria", examples=["nome_categoria"])
    
class CategoriaResponse(CategoriaBase):
    id_categoria: Optional[int] = Field(default=None, description="Id da categoria")
    
class CategoriaQuery(QueryMeta, CategoriaResponse):
    pass

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaCreate):
    descritivo_categoria: Optional[str] = Field(default=None, description="Nome da categoria")