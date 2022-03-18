import os
from aiogram import Bot, Dispatcher
import psycopg2 as ps
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cursor = base.cursor()

bot = Bot(token=os.environ.get('API_TOKEN'))
dp = Dispatcher(bot, storage=storage)
