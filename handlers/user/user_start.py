from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from createBot import bot
from postgreSQL import functions


class FSMStart(StatesGroup):
    check_age = State()
    load_id = State()
    select_location = State()
    select_area = State()


async def user_start(message: types.Message):
    await FSMStart.check_age.set()
    await message.reply('Check user. Enter your full ages:')


async def check_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await FSMStart.next()
    await message.reply('Upload a photo of your ID')


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMStart.next()
    await message.reply('Write your location')


async def select_location(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location'] = message.text
    await FSMStart.next()
    await message.reply('Write your area')


async def select_area(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['area'] = message.text
        data['user_id'] = 0

    await bot.send_message(message.from_user.id, 'Fine! After moderators check your application, you will get access '
                                                 'to all the functionality.')
    await functions.sql_add_user(state)
    await state.finish()


def register_message_start(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start-fsm'], state=None)
    dp.register_message_handler(check_age, state=FSMStart.check_age)
    dp.register_message_handler(load_id, content_types=['photo'], state=FSMStart.load_id)
    dp.register_message_handler(select_location, state=FSMStart.select_location)
    dp.register_message_handler(select_area, state=FSMStart.select_area)
