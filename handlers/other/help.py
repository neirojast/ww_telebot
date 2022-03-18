# Раздел для вспомогательных handler'ов вроде /help и /start
from aiogram import types, Dispatcher


async def other_help(message: types.Message):
    pass


async def register_handlers_other(dp: Dispatcher):
    pass
