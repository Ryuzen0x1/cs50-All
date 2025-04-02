cal_of_fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
  
name = input("Item: ").lower()  # Convert input to lowercase once

if name in cal_of_fruits:
    print("Calories:", cal_of_fruits[name])  # Direct dictionary lookup

# Your old code looping through the list
# for fruits in cal_of_fruits:
	# if name == fruits["fruit"]:
		# print("Calories:", fruits["calorie"])
	# else:
		# None
		# print("", sep="", end="")
