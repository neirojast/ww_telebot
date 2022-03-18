from typing import Union
from aiogram import types, Dispatcher
from keyboards.inlineKeyboards.inline_menu import menu_cd, brand_keyboard, items_keyboard, item_keyboard


async def show_menu(message: types.Message):
    await message.delete()
    await list_brands(message)


async def list_brands(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await brand_keyboard()

    if isinstance(message, types.Message):
        await message.answer('Here we have', reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text('Here we have', reply_markup=markup)


async def list_items(message: types.CallbackQuery):
    markup = await items_keyboard()


async def show_item(callback: types.CallbackQuery, category, item_id):
    markup = item_keyboard(item_id=item_id)
    text = 'Buy it'
    await callback.message.edit_text(text, reply_markup=markup)


async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    item_id = callback_data.get('item_id')

    level = {
        '0': list_brands,
        '1': list_items,
        '2': show_item,
    }

    current_level_function = level[current_level]

    await current_level_function(call, category=category, item_id=item_id)


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, commands=['menu'])
    dp.register_callback_query_handler(navigate, menu_cd.filter())
