from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from createBot import cursor


menu_cd = CallbackData('show_menu', 'level', 'brand_name', 'product_name', 'order_id')
select_order = CallbackData('buy', 'order_id')


def make_callback_data(level, brand_name='0', product_name='0', order_id='0'):
    return menu_cd.new(level=level, brand_name=brand_name, product_name=product_name, order_id=order_id)


async def brand_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    cursor.execute('SELECT brand_name FROM orders_card')
    for item in cursor:
        button_text = f'{item[0]}'
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1, brand_name=item[1])
        markup.insert(InlineKeyboardButton(text=button_text, callback_data=callback_data))

    return markup


async def items_keyboard(brand_name):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)
    query = 'SELECT product_name, price FROM order_cards WHERE brand_name = %s'
    cursor.execute(query, (brand_name,))
    for item in cursor:
        button_text = f'{item[0]}, {item[1]}'
        callback_data = make_callback_data(CURRENT_LEVEL + 1, )
    return markup


def item_keyboard(brand_name, item_id):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text='Buy', callback_data=select_order.new(order_id=item_id)))
    markup.insert(InlineKeyboardButton(text='Back to products', callback_data=make_callback_data(level=CURRENT_LEVEL - 1)))
    return markup
