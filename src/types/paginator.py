from abc import ABC, abstractmethod

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup


class Paginator(ABC):
    PAGINATE_BY: int = 5
    CALLBACK_DATA: CallbackData

    @classmethod
    @abstractmethod
    def create(cls, page: int, **kwargs) -> InlineKeyboardMarkup:
        pass
