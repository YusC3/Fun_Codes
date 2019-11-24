#Libraries used:
import random

favorite = "cheese"
least_favorite = "butter" 
full_menu = ["cheese", "orange", "soda",
             "butter", "banana", "potato"]

print("Here are all the menu options \n")
print("~ ~ ~ ~ ~ ~ ~ ~ ~")
print("~ ~ ~ ~ ~ ~ ~ ~ ~")
for item in full_menu:
    print(item)
print("~ ~ ~ ~ ~ ~ ~ ~ ~")
print("~ ~ ~ ~ ~ ~ ~ ~ ~")
print("\n")

round = 0

while round < 3:
    eaten = []
    current_menu = []
    items = 0

    print("Round", round + 1)
    print("- - - - - - - - \n")

    j = 0
    while j < 3:
        current_menu.append(random.choice(full_menu))
        j += 1

    print("Here are the current menu choices: ")
    print(current_menu)
    print("\n")

    for food in current_menu:
        if food == favorite:
            items += 3
            eaten.append(food)
        elif food == least_favorite:
            continue
        else:
            might_eat = random.randrange(0, 3)
            if might_eat > 0:
                eaten.append(food)
                items += might_eat

    print("This is how many items George ate in TOTAL this round: ")
    print(items, "\n")
    print("Here is what George ate from the current menu: ")
    print(eaten, "\n")
    print("- - - - - - - - ")

    round += 1
