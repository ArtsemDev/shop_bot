from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from src.keyboards.inline import CategoryInlineKeyboardMarkup

router = Router(name='user_category_router')


@router.message(F.text == '/category')
async def category_list(message: Message):
    await message.answer(
        text='CHOOSE CATEGORY',
        reply_markup=await CategoryInlineKeyboardMarkup.create()
    )


@router.callback_query(CategoryInlineKeyboardMarkup.CALLBACK_DATA.filter())
async def category_list(callback: CallbackQuery, callback_data: CategoryInlineKeyboardMarkup.CALLBACK_DATA):
    if callback_data.action == 'page':
        await callback.message.edit_reply_markup(
            reply_markup=await CategoryInlineKeyboardMarkup.create(page=callback_data.page)
        )
