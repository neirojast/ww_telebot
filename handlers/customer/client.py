from createBot import bot, cursor, base
from keyboards.replyKeyboards import start_kb
from aiogram import types, Dispatcher
from geopy import Nominatim
from postgreSQL import functions


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hi! I am WayWeedBot! Press "Buy" or "Sell"',
                           reply_markup=start_kb)
    sql_query = 'INSERT INTO users (user_id, user_role) VALUES (%s, %s)'
    string = "user"
    cursor.execute(sql_query, (message.from_user.id, string))
    base.commit()


async def get_call(message: types.Message):
    db = 'orders_card'
    await functions.sql_get_card(message, db)


async def seller_call(callback: types.CallbackQuery):
    await callback.message.answer(f'OK! You are Seller!')
    string = "seller"
    sql_query = 'UPDATE users SET user_role = (%s) WHERE user_id = (%s)'
    cursor.execute(sql_query, (string, callback.from_user.id))
    base.commit()
    await callback.answer()


async def customer_call(callback: types.CallbackQuery):
    await callback.message.answer(f'OK! You are Customer!')
    string = "customer"
    sql_query = 'UPDATE users SET user_role = (%s) WHERE user_id = (%s)'
    cursor.execute(sql_query, (string, callback.from_user.id))
    base.commit()
    await callback.answer()


async def send_location(message: types.Message):
    if message.location is not None:
        await bot.send_message(message.from_user.id, f'Latitude: {message.location.latitude}\n'
                                                     f'Longitude: {message.location.longitude}')
    geolocator = Nominatim(user_agent='MyApp')
    location = geolocator.geocode(f'{message.location.latitude}, {message.location.longitude}')
    await bot.send_message(message.from_user.id, f'Ваша предполагаемая геолокация: {location}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(get_call, commands=['qwer'])
    dp.register_callback_query_handler(seller_call, text='seller')
    dp.register_callback_query_handler(customer_call, text='customer')
    dp.register_message_handler(send_location, content_types=['location'])
