from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    queijo_muss_ing = Ingredient('queijo mussarela')
    bacon = Ingredient('bacon')

    assert queijo_muss_ing.name == "queijo mussarela"

    assert queijo_muss_ing.__repr__() == "Ingredient('queijo mussarela')"

    assert (queijo_muss_ing == bacon) == False

    assert (queijo_muss_ing == queijo_muss_ing) == True

    assert queijo_muss_ing.__hash__() != bacon.__hash__()

    assert queijo_muss_ing.__hash__() == queijo_muss_ing.__hash__()

    expected_restrictions_queijo_muss = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    assert queijo_muss_ing.restrictions == expected_restrictions_queijo_muss
    