from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from createBot import cursor
from aiogram import Dispatcher, types
from postgreSQL import functions


class FSMAdmin(StatesGroup):
    photo = State()
    brand_name = State()
    product_name = State()
    description = State()
    price = State()


async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Load photo')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Load brand name')


async def load_brand_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['brand_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Load product name')


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Load description')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Load price for 1/8 oz')


async def load_price(message: types.Message, state: FSMContext):
    cursor.execute('SELECT MAX(order_id) FROM order_cards')
    order_id = cursor.fetchone()[0]
    async with state.proxy() as data:
        data['price'] = float(message.text)
        data['order_id'] = order_id+1
    await functions.sql_add_order_card(state)
    await state.finish()


def register_handlers_cards(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Load'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_brand_name, state=FSMAdmin.brand_name)
    dp.register_message_handler(load_product_name, state=FSMAdmin.product_name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
