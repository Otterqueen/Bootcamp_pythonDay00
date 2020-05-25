import sys


cookbook = {'sandwich': {
                'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': "lunch",
                'prep_time': 10},
            'cake': {
                'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': "dessert",
                'prep_time': 60},
            'salad': {
                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                'meal': "lunch",
                'prep_time': 15}
            }


def print_recipe(name):
    if (name in cookbook):
        print("\n\nRecipe for ", name, " :")
        print("Ingredients list: {ingredients} \n\
To be eaten for {meal}.\n\
Takes {prep_time} minutes of cooking.\n\n".format(**cookbook[name]))
    else:
        print("\n\nThis recipe doesn't exist. Do you want to create it ?\n")


def del_recipe(name):
    del cookbook[name]


def create_recipe(name, i, m, p):
    if (name in cookbook):
        print("\n\nThis recipe already exist.\n\n")
    else:
        cookbook.update({name: {"ingredients": i, "meal": m, "prep_time": p}})
        print("Bravo! Recette sauvegardée!\n\n")


def print_cookbook():
    print("Here, the list of all the recipes in this cookbook : \n")
    for key in cookbook:
        print("{:s}".format(key))


while 1:
    input_user = input("\nPlease select an option by typing the \
corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n")
    if input_user == '1':
        name = input("\nPlease enter the recipe's name to create it:\n")
        ingredients = input("\nPlease enter the ingredients of the repice: \
(Syntaxe is : ingredient1, ingredient2, ingredient3) \n")
        meal = input("\nPlease enter the type of meal of the repice: \n")
        prep_time = input("\nPlease enter the prep_time of the repice: \n")
        create_recipe(name, ingredients.split(", "), meal, prep_time)
    elif input_user == '2':
        name = input("\nPlease enter the recipe's name to delete it:\n")
        del_recipe(name)
    elif input_user == '3':
        name = input("\nPlease enter the recipe's name to get its details:\n")
        print_recipe(name)
    elif input_user == '4':
        print_cookbook()
    elif input_user == '5':
        print("\nCookbook closed.")
        sys.exit()
    else:
        print("\n\nThis option does not exist, please type the \
corresponding number.\nTo exit, enter 5.\n\n")
