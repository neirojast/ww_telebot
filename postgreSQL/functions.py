from createBot import cursor, base
from createBot import bot


async def get_cell(column, row, parameter):
    # sql query to get current cell from current table
    query = 'SELECT * FROM %s WHERE %s = %s'
    [value], = cursor.execute(query, (column, row, parameter))
    return str(value)


async def sql_add_order_card(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO order_cards (img, brand_name, product_name, description, price, order_id) '
                       'VALUES (%s, %s, %s, %s, %s, %s)', tuple(data.values()))
        base.commit()


async def sql_add_user(state):
    async with state.proxy() as data:
        sql_query = 'INSERT INTO users_cards (age, img, location, area, user_id) ' \
                    'VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(sql_query, (tuple(data.values())))
        base.commit()


async def sql_read(message):
    cursor.execute('SELECT * FROM orders_card')
    for ret in cursor:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n{ret[2]}\nPrice for 1 oz: {ret[3]}')


async def sql_get_order_card(message, order_id):
    query = 'SELECT * FROM order_cards WHERE order_id = %s'
    cursor.execute(query, (order_id,))
    for ret in cursor:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[2]}\n{ret[3]}\n{ret[4]}')


async def check_user_role(message, user_id):
    pass
