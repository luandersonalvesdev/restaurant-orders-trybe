from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
from models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    dish_strogonof = Dish("Strogonof", 15.00)
    dish_salad = Dish("Salad", 11.00)

    assert dish_strogonof.name == "Strogonof"

    assert dish_strogonof != dish_salad

    assert dish_strogonof == dish_strogonof

    assert (dish_strogonof.__hash__() != dish_salad.__hash__())

    assert (dish_strogonof.__hash__() == dish_strogonof.__hash__())

    with pytest.raises(TypeError):
        Dish("Strogonof", "15")

    with pytest.raises(ValueError):
        Dish("Strogonof", -1)

    assert dish_strogonof.__repr__() == "Dish('Strogonof', R$15.00)"

    queijo_muss_ing = Ingredient("queijo mussarela")

    dish_strogonof.add_ingredient_dependency(queijo_muss_ing, 5)

    assert dish_strogonof.get_ingredients() == {queijo_muss_ing}

    restrictions_queijo_muss = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_strogonof.get_restrictions() == restrictions_queijo_muss
