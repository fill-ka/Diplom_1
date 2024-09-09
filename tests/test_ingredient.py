import pytest
from practikum.ingredient import Ingredient


@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "hot sauce", 100),
    ("FILLING", "cutlet", 150),
])
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
