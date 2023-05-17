
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

#retrieves names from list of foods.
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

#returns foods with a heat_level over 5.
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 4]

#returns all foods formatted with 🌶  emojis. 
#Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶' }")

#returns the food that matches a cuisine. 
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

#returns foods with heat_level over 5 formatted with 🌶  emojis.
#Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶' }")

#returns average of heat_levels in spicy_foods.
def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:
        sum += food['heat_level']
    return sum / len(spicy_foods)

#returns original list of spicy_foods with new spicy_food added.
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
