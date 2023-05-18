from math import ceil

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pydantic import Field
from sqlalchemy import select
from sqlalchemy.sql.functions import count

from src.models import Category
from src.types import Paginator


class CategoryCallbackData(CallbackData, prefix='category'):
    category_id: int = Field(ge=1, default=None)
    page: int = Field(ge=1, default=1)
    parent_id: int = Field(ge=1, default=None)
    action: str


class CategoryInlineKeyboardMarkup(Paginator):

    PAGINATE_BY = 5
    CALLBACK_DATA = CategoryCallbackData

    @classmethod
    async def create(cls, page: int = 1, parent_id: int = None) -> InlineKeyboardMarkup:
        async with Category.async_session() as session:
            count_category = await session.scalar(
                select(count(Category.id))
                .filter_by(parent_id=parent_id)
            )
        max_page = ceil(count_category / cls.PAGINATE_BY)

        async with Category.async_session() as session:
            categories = await session.scalars(
                select(Category)
                .order_by(Category.id)
                .filter_by(parent_id=parent_id)
                .limit(cls.PAGINATE_BY)
                .offset(page * cls.PAGINATE_BY - cls.PAGINATE_BY)
            )
            buttons = [
                [
                    InlineKeyboardButton(
                        text=category.name,
                        callback_data=cls.CALLBACK_DATA(
                            category_id=category.id,
                            page=1,
                            parent_id=category.parent_id,
                            action='get'
                        ).pack()
                    )
                ]
                for category in categories.all()
            ]
        if buttons:
            buttons += [
                [
                    InlineKeyboardButton(
                        text='◀️',
                        callback_data=cls.CALLBACK_DATA(
                            parent_id=parent_id,
                            page=(page - 1) if page > 1 else max_page,
                            action='page'
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text='️️▶️',
                        callback_data=cls.CALLBACK_DATA(
                            parent_id=parent_id,
                            page=(page + 1) if page < max_page else 1,
                            action='page'
                        ).pack()
                    )
                ]
            ]
            return InlineKeyboardMarkup(inline_keyboard=buttons)
