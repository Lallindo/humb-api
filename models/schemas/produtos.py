from pydantic import Field, field_validator, BaseModel as Base
from typing import List, Optional
from core import QueryMeta
from .categorias import CategoriaBase
from .imagens import ImagemURL

class ProdutoBase(Base):
    descritivo_produto: Optional[str] = Field(default="", description="Nome do produto", examples=["nome_produto"])
    descricao_produto: Optional[str] = Field(default="", description="", examples=[""])
    preco_produto: Optional[float] = Field(default=0, description="")
    desconto_produto: Optional[float] = Field(default=0, description="")
    estoque_produto: Optional[int] = Field(default=0, description="")
    ativo_produto: Optional[bool] = Field(default=1, description="")
    
class ProdutoResponse(ProdutoBase):
    id_produto: Optional[int] = Field(default=None, description="ID do produto")
    imagens: List[ImagemURL] = Field(description="Imagens do produto")
    categorias: List[CategoriaBase] = Field(description="Categoria(s) do produto")
    
class ProdutoQuery(QueryMeta, ProdutoBase):
    id_produto: Optional[int] = Field(default=None, description="ID do produto")

class ProdutoCreate(ProdutoBase):
    imagens: List[ImagemURL] = Field(description="Imagens do produto")

class ProdutoUpdate(ProdutoCreate):
    descritivo_produto: Optional[str] = Field(default=None, description="Nome do produto")