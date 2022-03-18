from aiogram import types, Dispatcher
from createBot import cursor, base


async def echo_send(message: types.Message):
    if message.text == '123-456':
        cursor.execute('DELETE FROM users')
        base.commit()
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
