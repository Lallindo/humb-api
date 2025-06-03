from sqlalchemy import String, ForeignKey, DECIMAL, Enum, Date, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy
from typing import get_args, Literal, List, Optional
import datetime
import enum
from database import Base

"""
    -- Produtos --
    
    Dados abaixo estarão diretamente ligados com a existência de produtos no site
"""

class ProdutosDB(Base):
    __tablename__ = "produtos"
    
    id_produto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    descritivo_produto: Mapped[str] = mapped_column(String(300))
    descricao_produto: Mapped[str] = mapped_column(String(2000))
    preco_produto: Mapped[DECIMAL] = mapped_column(DECIMAL(precision=2))
    desconto_produto: Mapped[int] = mapped_column()
    estoque_produto: Mapped[int] = mapped_column()
    ativo_produto: Mapped[bool] = mapped_column(default=True)
    
    imagens: Mapped["ImagensDB"] = relationship()
    categorias: Mapped["CategoriasDB"] = relationship(secondary="em_categoria", back_populates="produtos")
    
class ImagensDB(Base):
    __tablename__ = "imagens"
    
    id_img: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    url_img: Mapped[str] = mapped_column(String(1000))
    id_produto_fk: Mapped[int] = mapped_column(ForeignKey("produtos.id_produto"))
    
class CategoriasDB(Base):
    __tablename__ = "categorias"
    
    id_categoria: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    descritivo_categoria: Mapped[str] = mapped_column(String(100))
    
    produtos: Mapped["ProdutosDB"] = relationship(secondary="em_categoria", back_populates="categorias")
    
class EmCategoriaDB(Base):
    __tablename__ = "em_categoria"
    
    id_em_categoria: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_prod_fk: Mapped[int] = mapped_column(ForeignKey("produtos.id_produto"))
    id_categoria_fk: Mapped[str] = mapped_column(ForeignKey("categorias.id_categoria"))
    
# -- Fim Produtos -- #

"""
    -- Usuários --
    
    Dados abaixo estarão diretamente ligados com a existência de usuários no site
"""

class GeneroEnum(enum.StrEnum):
    MASCULINO = enum.auto()
    FEMININO = enum.auto()
    OUTRO = enum.auto()
    
class UnidadesFederativasEnum(enum.StrEnum):
    AC = enum.auto()
    AL = enum.auto()
    AP = enum.auto()
    AM = enum.auto()
    BA = enum.auto()
    CE = enum.auto()
    ES = enum.auto()
    GO = enum.auto()
    DF = enum.auto()
    MA = enum.auto()
    MT = enum.auto()
    MS = enum.auto()
    MG = enum.auto()
    PA = enum.auto()
    PB = enum.auto()
    PR = enum.auto()
    PE = enum.auto()
    PI = enum.auto()
    RJ = enum.auto()
    RN = enum.auto()
    RS = enum.auto()
    RO = enum.auto()
    RR = enum.auto()
    SC = enum.auto()
    SP = enum.auto()
    SE = enum.auto()
    TO = enum.auto()

class UsuariosDB(Base):
    __tablename__ = "usuarios"
    
    id_usuario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    nome_usuario: Mapped[int] = mapped_column(String(200))
    genero_usuario: Mapped[GeneroEnum] = mapped_column(Enum(GeneroEnum))
    cpf_usuario: Mapped[str] = mapped_column(String(11))
    
    telefones: Mapped["TelefonesDB"] = relationship()
    enderecos: Mapped["EnderecosDB"] = relationship()
    
class TelefonesDB(Base):
    __tablename__ = "telefones"
    
    id_telefone: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_usuario_fk: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"))
    numero_telefone: Mapped[str] = mapped_column(String(20))
    
class EnderecosDB(Base):
    __tablename__ = "enderecos"
    
    id_endereco: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_usuario_fk: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"))
    numero_endereco: Mapped[str] = mapped_column(String(10))
    rua_endereco: Mapped[str] = mapped_column(String(1000))
    bairro_endereco: Mapped[str] = mapped_column(String(1000))
    cidade_endereco: Mapped[str] = mapped_column(String(100))
    descricao_endereco: Mapped[str] = mapped_column(String(1000))
    uf_endereco: Mapped[UnidadesFederativasEnum] = mapped_column(Enum(UnidadesFederativasEnum))
    
# -- Fim Usuários -- #

"""
    -- Pedidos --
    
    Dados abaixo juntam as estruturas de usuários e produtos para criar o sistema de pedidos e compras
"""

class TiposPagamentoEnum(enum.StrEnum):
    PIX = enum.auto()
    TRANSF_BANC = enum.auto()

class PedidosDB(Base):
    __tablename__ = "pedidos"
    
    id_pedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_usuario_fk: Mapped[int] = mapped_column(ForeignKey("usuarios.id_usuario"))
    data_criacao_pedido: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    data_ultima_alteracao_pedido: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    data_finalizacao_pedido: Mapped[Optional[datetime.datetime]] = mapped_column()
    tipo_pagamento: Mapped[Optional[TiposPagamentoEnum]] = mapped_column(Enum(TiposPagamentoEnum))
    
    produtos: Mapped[ProdutosDB] = relationship(secondary="em_pedido")
    
class EmPedidoDB(Base):
    __tablename__ = "em_pedido"
    
    id_em_pedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    id_pedido_fk: Mapped[int] = mapped_column(ForeignKey("pedidos.id_pedido"))
    id_produto_fk: Mapped[int] = mapped_column(ForeignKey("produtos.id_produto"))
    quant_produto_em_pedido: Mapped[int] = mapped_column()

# -- Fim Pedidos -- #
