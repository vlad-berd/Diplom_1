import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from data import *


@pytest.fixture()
def burger():
    return Burger()

@pytest.fixture()
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = bun_data['name']
    mock_bun.price = bun_data['price']
    mock_bun.get_name.return_value = bun_data['name']
    mock_bun.get_price.return_value = bun_data['price']

    return mock_bun

@pytest.fixture()
def ingredient_sauce_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = ingredient_sauce_data['type']
    mock_ingredient.name = ingredient_sauce_data['name']
    mock_ingredient.price = ingredient_sauce_data['price']
    mock_ingredient.get_price.return_value = ingredient_sauce_data['price']
    mock_ingredient.get_name.return_value = ingredient_sauce_data['name']
    mock_ingredient.get_type.return_value = ingredient_sauce_data['type']

    return mock_ingredient

@pytest.fixture()
def ingredient_filling_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = ingredient_filling_data['type']
    mock_ingredient.name = ingredient_filling_data['name']
    mock_ingredient.price = ingredient_filling_data['price']
    mock_ingredient.get_price.return_value = ingredient_filling_data['price']
    mock_ingredient.get_name.return_value = ingredient_filling_data['name']
    mock_ingredient.get_type.return_value = ingredient_filling_data['type']

    return mock_ingredient
