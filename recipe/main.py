from recipe import Recipe


def create_recipe(name, coffee=0, chocolate=0, sugar=0, milk=0, price=0):
    recipe = Recipe(name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    return recipe


recipe1 = create_recipe("Coffee with sugar",
                        coffee=4, sugar=2, milk=0, price=30.0)
recipe2 = create_recipe("Latte", coffee=3,
                        sugar=5, milk=5, price=50.0)
recipe3 = create_recipe("Hot Chocolate", chocolate=3,
                        sugar=2, milk=2, price=20.0)
print(recipe1)
print(recipe2)
print(recipe3)
