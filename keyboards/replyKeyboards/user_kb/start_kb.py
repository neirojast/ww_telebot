from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = InlineKeyboardMarkup(row_width=2)
sell_bttn = InlineKeyboardButton(text='Sell', callback_data='seller')
buy_bttn = InlineKeyboardButton(text='Buy', callback_data='customer')
start_kb.row(sell_bttn, buy_bttn)


start_kb_locate = InlineKeyboardMarkup(row_width=1)
loc_bttn_1 = InlineKeyboardButton(text='Torronto', callback_data='tor')
loc_bttn_2 = InlineKeyboardButton(text='Montreal', callback_data='mon')
loc_bttn_3 = InlineKeyboardButton(text='Vancouvert', callback_data='can')
loc_bttn_4 = InlineKeyboardButton(text='Ottava', callback_data='ott')
start_kb_locate.row(loc_bttn_1, loc_bttn_2, loc_bttn_3, loc_bttn_4)


start_kb_area = InlineKeyboardMarkup(row_width=2)
area_bttn_1 = InlineKeyboardButton(text='I', callback_data='I-area')
area_bttn_2 = InlineKeyboardButton(text='II', callback_data='II-area')
area_bttn_3 = InlineKeyboardButton(text='III', callback_data='III-area')
area_bttn_4 = InlineKeyboardButton(text='IV', callback_data='IV-area')
area_bttn_5 = InlineKeyboardButton(text='V', callback_data='V-area')
start_kb_area.row(area_bttn_1, area_bttn_2, area_bttn_3, area_bttn_4, area_bttn_5)