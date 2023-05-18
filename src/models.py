from sqlalchemy import Column, SMALLINT, VARCHAR, ForeignKey, DECIMAL, BIGINT

from .database import Base


class Category(Base):
    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True, index=True)
    slug = Column(VARCHAR(64), nullable=False, unique=True, index=True)
    parent_id = Column(SMALLINT, ForeignKey('category.id', ondelete='RESTRICT'), nullable=True)

    def __repr__(self):
        return self.name


class Product(Base):
    name = Column(VARCHAR(128), nullable=False, unique=True, index=True)
    slug = Column(VARCHAR(128), nullable=False, unique=True, index=True)
    description = Column(VARCHAR(2048), nullable=True)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(SMALLINT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    image = Column(VARCHAR(256), nullable=True)

    def __repr__(self):
        return self.name


class Shop(Base):
    id = Column(SMALLINT, primary_key=True)
    address = Column(VARCHAR(256), nullable=False)

    def __repr__(self):
        return self.address


class ShopProduct(Base):
    shop_id = Column(SMALLINT, ForeignKey('shop.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(BIGINT, ForeignKey('shop.id', ondelete='CASCADE'), nullable=False)
    count = Column(SMALLINT, nullable=False, default=0, server_default='0')
