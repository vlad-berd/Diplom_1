from praktikum.ingredient_types import *


bun_data = {
    "name": 'Флюоресцентная булка R2-D3',
    "price":  988
}

ingredient_sauce_data = {
    "type": INGREDIENT_TYPE_SAUCE,
    "name": 'Соус Spicy-X',
    "price":  90
}

ingredient_filling_data = {
    "type": INGREDIENT_TYPE_FILLING,
    "name": 'Мясо бессмертных моллюсков Protostomia',
    "price":  1337
}

expected_value_get_price_with_one_bun_and_one_filling = (bun_data['price'] * 2 + ingredient_filling_data['price'])

excepted_value_get_receipt_only_with_one_bun = (f'(==== {bun_data['name']} ====)\n'
                        f'(==== {bun_data['name']} ====)\n'
                        f'\n'
                        f'Price: {bun_data['price'] * 2}')

excepted_value_get_receipt_with_bun_and_one_filling = (f'(==== {bun_data['name']} ====)\n'
                        f'= {ingredient_filling_data['type'].lower()} {ingredient_filling_data['name']} =\n'
                        f'(==== {bun_data['name']} ====)\n'
                        f'\n'
                        f'Price: {bun_data['price'] * 2 + ingredient_filling_data['price']}')

excepted_value_get_receipt_with_bun_and_one_sauce = (f'(==== {bun_data['name']} ====)\n'
                        f'= {ingredient_sauce_data['type'].lower()} {ingredient_sauce_data['name']} =\n'
                        f'(==== {bun_data['name']} ====)\n'
                        f'\n'
                        f'Price: {bun_data['price'] * 2 + ingredient_sauce_data['price']}')
