from pydantic import Field, field_validator, BaseModel as Base
from typing import List, Optional
from core import QueryMeta
from .categorias import CategoriaBase
from .imagens import ImagemURL

class ProdutoBase(Base):
    descritivo_produto: Optional[str] = Field(default="", description="Nome do produto", examples=["nome_produto"])
    descricao_produto: Optional[str] = Field(default="", description="", examples=[""])
    preco_produto: Optional[str] = Field(default="", description="", examples=[""])
    desconto_produto: Optional[str] = Field(default="", description="", examples=[""])
    estoque_produto: Optional[str] = Field(default="", description="", examples=[""])
    ativo_produto: Optional[str] = Field(default="", description="", examples=[""])
    
class ProdutoResponse(ProdutoBase):
    id_produto: Optional[int] = Field(default=None, description="ID do produto")
    imagens: List[ImagemURL] = Field(description="Imagens do produto")
    categorias: List[CategoriaBase] = Field(description="Categoria(s) do produto")
    
class ProdutoQuery(QueryMeta, ProdutoBase):
    id_produto: Optional[int] = Field(default=None, description="ID do produto")

class ProdutoCreate(ProdutoBase):
    imagens: List[ImagemURL] = Field(description="Imagens do produto")
    
    @field_validator("images", mode="before")
    def remodel_children(self, _, value) -> ImagemURL:
        if value and isinstance(value, dict):
            return ImagemURL(**value)
        return value

class ProdutoUpdate(ProdutoCreate):
    descritivo_produto: Optional[str] = Field(default=None, description="Nome do produto")