## Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающий класс `Burger`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

Тестовые методы class TestBurger:
1. test_set_buns_success
2. test_add_ingredient_success
3. test_remove_ingredient_success
4. test_move_ingredient_success
5. test_get_price_only_with_bun_success
6. test_get_price_with_bun_and_one_ingredient_success
7. test_get_receipt_only_with_one_bun_success
8. test_get_receipt_success

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`