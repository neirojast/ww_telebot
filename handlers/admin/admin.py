from createBot import Dispatcher, bot, cursor, base
from aiogram import types
from keyboards import users_kb
from postgreSQL import functions


async def show_users_count(message: types.Message):
    cursor.execute('SELECT COUNT(*) FROM users')
    users_count = cursor.fetchone()
    await bot.send_message(message.from_user.id, f'Кол-во пользователей: {users_count[0]}', reply_markup=users_kb)


async def show_orders(message: types.Message):
    await functions.sql_read(message)
    cursor.execute('SELECT COUNT(*) FROM orders_card')
    orders_count = cursor.fetchone()
    await bot.send_message(message.from_user.id, f'Количество карточек: {orders_count[0]}')


async def show_all_admins(message: types.Message):
    cursor.execute("SELECT user_id FROM users WHERE user_role='admin'")
    resoults = cursor.fetchall()
    for ret in resoults:
        await bot.send_message(message.from_user.id, f'{ret[0]}')


async def show_all_moderators(message: types.Message):
    cursor.execute("SELECT user_id FROM users WHERE user_role='moderator'")
    resoults = cursor.fetchall()
    for ret in resoults:
        await bot.send_message(message.from_user.id, f'{ret[0]}')


async def show_all_customers(message: types.Message):
    cursor.execute("SELECT user_id FROM users WHERE user_role='customer'")
    resoults = cursor.fetchall()
    for ret in resoults:
        await bot.send_message(message.from_user.id, f'{ret[0]}')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(show_users_count, commands=['Users'])
    dp.register_message_handler(show_orders, commands=['Orders'])
    dp.register_message_handler(show_all_admins, commands=['admins'])
    dp.register_message_handler(show_all_moderators, commands=['moderators'])
    dp.register_message_handler(show_all_customers, commands=['customers'])
