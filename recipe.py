#!/usr/bin/env python3.6


# a personal project to test my understanding using list, if statements and for loop


masala_chicken = [
    "MARINATION",
    "1 whole chicken",
    "Red Chilli powder 1/2 tsp",
    "Tumeric powder 1/4 tsp",
    "Garam masala 1 tsp",
    "low fat yoghurt 4 tbsp",
    "1 cm chop ginger",
    "6 cloves garlic",
    "---------------------------------",
    "SPICE POWDER IN THE CURRY",
    "Turmeric powder- 1/2 tsp",
    "Red Chilli Powder- 1/2 tsp",
    "Pav Bhaji Masala- 1 tsp",
    "Coriander seeds 2 tsp",
    "Cumin seeds seeds 2 tsp",
    "Garam Masala powder- 1 tsp",
    "Green chilli - 8-9",
    "Coriander leaves"
    "---------------------------------"
]

ayam_rendang = [
    "Fine grind ingredients",
    "8 shallots",
    "6 cloves garlic",
    "3 lemongrass stems",
    "3 inch ginger",
    "3 inch galangal",
    "3 pieces of turmeric live"
    "Red chili and Bird's eye chilli",
    "4 pieces of candle nut",
    "1 big red onion",
    "-----------------------------------",
    "Other ingredients",
    "1 cup of dried chilli paste",
    "4 pieces of lime leaves"
    "1 chicken, cut into small pieces",
    "1 1/2 seed extract of coconut milk",
    "4 tbsp kerisik (grated and toasted coconut then ground to a paste)",
    "2-3 pieces asam gelugur (can be substitute with tamarind paste)",
    "Salt and sugar to taste",
    "Fine slices of turmeric leaves"

]

recipe = input("What recipe do you want? : ")

if recipe == "masala chicken":
    for ingredient in masala_chicken:
        print(ingredient)
elif recipe == "rendang chicken":
    for ingredient in ayam_rendang:
        print(ingredient)
else:
    print("Recipe is not available")
