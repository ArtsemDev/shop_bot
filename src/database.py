from sqlalchemy import Column, BIGINT
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr

from loader import SETTINGS


class Base(DeclarativeBase):

    id = Column(BIGINT, primary_key=True)

    _async_engine = create_async_engine(SETTINGS.DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://'))
    async_session = async_sessionmaker(bind=_async_engine)

    @declared_attr
    def __tablename__(cls) -> str:
        return ''.join([f'_{i.lower()}' if i.isupper() else i for i in cls.__name__]).strip('_')
