import os
from aiogram import executor
from createBot import bot
from createBot import dp
from handlers.seller import add_new_card
from handlers.user import user_start
from handlers.customer import client
from createBot import base, cursor


async def on_startup(dp):
    await bot.set_webhook(os.environ.get('URL_APP'))


async def on_shutdown(dp):
    await bot.delete_webhook()
    cursor.close()
    base.close()

user_start.register_message_start(dp)
client.register_handlers_client(dp)
add_new_card.register_handlers_cards(dp)


executor.start_webhook(dispatcher=dp,
                       webhook_path='',
                       on_startup=on_startup,
                       on_shutdown=on_shutdown,
                       skip_updates=True,
                       host='0.0.0.0',
                       port=int(os.environ.get('PORT'))
                       )
