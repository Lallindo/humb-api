from pydantic import Field, BaseModel as Base
from typing import List, Optional
from core import QueryMeta

class ImagemURL(Base):
    url_imagem: str = Field(description="URL da imagem do produto")
    