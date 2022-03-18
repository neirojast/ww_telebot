from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True)

registration_bttn = KeyboardButton('/r')
order_cards_bttn = KeyboardButton('/o')

user_kb.row(registration_bttn, order_cards_bttn)
