from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.format_dishes(source_path)

    def format_dishes(self, source_path):
        dishes = {}
        with open(source_path, encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",", quotechar='"')

            _, *data = csvreader
            for dish, price, ingredient, recipe_amount in data:

                if dish not in dishes:
                    dishes[dish] = Dish(dish, float(price))
                dish = dishes[dish]
                dish.add_ingredient_dependency(
                    Ingredient(ingredient), int(recipe_amount)
                    )

        return set(dishes.values())
