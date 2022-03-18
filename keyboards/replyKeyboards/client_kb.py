from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

client_kb = ReplyKeyboardMarkup(resize_keyboard=True)

b3 = KeyboardButton('/Users')
b4 = KeyboardButton('/Load')
b5 = KeyboardButton('/Delete')
b6 = KeyboardButton('/Orders')
button_inline = KeyboardButton('/Inline')
button_location = KeyboardButton('Send my location', request_location=True)

client_kb.row(b3).row(b4, b5, b6).row(button_inline, button_location)
