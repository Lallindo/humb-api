from pydantic import Field, BaseModel as Base
from typing import List, Optional
import enum

class TiposPagamentoEnum(enum.StrEnum):
    PIX = enum.auto()
    TRANSF_BANC = enum.auto()

class PedidoBase(Base):
    data_criacao_pedido: Optional[str] = Field()
    data_ultima_alteracao_pedido: Optional[str] = Field()
    data_finalizacao_pedido: Optional[str] = Field()
    tipo_pagamento: Optional[TiposPagamentoEnum] = Field(default=None, description="Tipo de pagamento selecionado")

class PedidoId(Base):
    id_pedido: Optional[int] = Field(default=None, description="Id do pedido")

class PedidoResponse(PedidoBase, PedidoId):
    pass