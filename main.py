import random

subjects = [
    "Ananya Pandey",
    "Khushi Kapoor",
    "Kriti Sanon",
    "A Mumbai Persian Cat",
    "A Group of Monkeys",
    "President Draupadi Murmu",
    "Truck Driver from Haryana"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war",
    "celebrates",
    "orders"
]

places_or_things = [
    "at Victoria Memorial",
    "in Mumbai Local Train",
    "a plate of papdi chat",
    "inside The Parliament",
    "at Sarojini Market",
    "during Durga Puja",
    "at Wagha Border"
]

# start headline generation using while loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "  #concatenation
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ".strip().lower())
    if user_input == "no":
        break

print("\nThank you for using the Fake Headline Generator, have a fun day ahead!")

