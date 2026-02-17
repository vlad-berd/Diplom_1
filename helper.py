from unittest.mock import Mock


def create_ingredient_mock(type, name, price):
    mock_ingredient = Mock()
    mock_ingredient.type = type
    mock_ingredient.name = name
    mock_ingredient.price = price
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_type.return_value = type

    return mock_ingredient