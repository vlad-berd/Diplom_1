from data import *


class TestBurger:
    def test_set_buns_success(self, burger, bun_mock):
        mock_bun = bun_mock

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
    
    def test_add_ingredient_success(self, burger, ingredient_sauce_mock):
        mock_ingredient_sauce = ingredient_sauce_mock

        burger.add_ingredient(mock_ingredient_sauce)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_success(self, burger, ingredient_sauce_mock, ingredient_filling_mock):
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)

        burger.remove_ingredient(0)

        assert burger.ingredients[0].name == ingredient_filling_mock.name
    
    def test_move_ingredient_success(self, burger, ingredient_sauce_mock, ingredient_filling_mock):
        burger.add_ingredient(ingredient_sauce_mock)
        burger.add_ingredient(ingredient_filling_mock)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[1].name == ingredient_sauce_mock.name

    def test_get_price_only_with_bun_success(self, burger, bun_mock):
        mock_bun = bun_mock
        burger.set_buns(mock_bun)

        burger_price = burger.get_price()

        assert burger_price == mock_bun.price * 2
    
    def test_get_price_with_bun_and_one_ingredient_success(self, burger, bun_mock, ingredient_filling_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_filling_mock)

        burger_price = burger.get_price()

        assert burger_price == expected_value_get_price_with_one_bun_and_one_filling

    def test_get_receipt_only_with_one_bun_success(self, burger, bun_mock):
        burger.set_buns(bun_mock)

        receipt = burger.get_receipt()
        
        assert receipt == excepted_value_get_receipt_only_with_one_bun

    def test_get_receipt_success(self, burger, bun_mock, ingredient_filling_mock):
        burger.set_buns(bun_mock)

        burger.add_ingredient(ingredient_filling_mock)
        
        receipt = burger.get_receipt()
        
        assert receipt == excepted_value_get_receipt_with_bun_and_one_filling