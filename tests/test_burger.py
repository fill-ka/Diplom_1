from unittest.mock import Mock
from practikum.burger import Burger
from practikum.ingredient import Ingredient
from practikum.bun import Bun


def test_burger_get_receipt():
    # Создаем mock-объекты
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100  # Устанавливаем цену булки

    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_price.return_value = 20  # Устанавливаем цену ингредиента

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    # Получаем рецепт
    receipt = burger.get_receipt()

    # Проверяем корректную цену (100 за каждую из двух булок + 20 за ингредиент)
    assert 'Price: 120' in receipt  # Ожидаемая цена: 100 (верхняя булка) + 100 (нижняя булка) + 20 (ингредиент)
