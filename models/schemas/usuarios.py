from pydantic import Field, BaseModel as Base
from typing import List, Optional
from core import QueryMeta
import enum

class GeneroEnum(enum.StrEnum):
    MASCULINO = enum.auto()
    FEMININO = enum.auto()
    OUTRO = enum.auto()

class UsuarioBase(Base):
    nome_usuario: Optional[str] = Field(default="", description="Nome do usuário", examples=["nome_usuario"])
    genero_usuario: Optional[GeneroEnum]
    
class UsuarioResponse(UsuarioBase):
    id_usuario: Optional[int] = Field(default=None, description="Id do usuário")
    
class UsuarioQuery(QueryMeta, UsuarioResponse):
    pass

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioCreate):
    descritivo_usuario: Optional[str] = Field(default=None, description="Nome da Usuario")