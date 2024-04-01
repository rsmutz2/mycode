#!/usr/bin/env python3
"""Bible Character Facts | Script prompts user to choose from list of Biblical names, then randomly prints 1 of 2 interesting facts about the character using if, elif, and else statements."""


import random

biblical_names = ["Adam", "Eve", "Moses", "Sarah", "David"]

print("Choose a Biblical name from the list:")
for name in biblical_names:
    print(name)

user_choice = input("Enter your choice: ")

if user_choice in biblical_names:
    if user_choice == "Adam":
      facts = ["Adam is the first human God created.",
               "Adam and his wife, Eve, were the first couple in the Bible."]
    elif user_choice == "Eve":
      facts = ["Eve was the first woman God created.",
               "Eve was tempted by the serpent to eat the fruit God commanded her not to eat."]
    elif user_choice == "Moses":
      facts = ["Moses led the Israelites out of Egypt.",
               "Moses received the Ten Commandments on Mount Sinai."]
    elif user_choice == "Sarah":
      facts = ["Sarah was the wife of Abraham.",
               "Sarah gave birth to Isaac in her old age. Even at 90 years old!"]
    elif user_choice == "David":
      facts = ["David was the second king of Israel, next after Saul.",
               "David defeated the giant Goliath with a sling and a stone in the Valley of Elah."]
    
    random_fact = random.choice(facts)
    
    print("Did you know?")
    print(random_fact)
else:
    print("Invalid choice. Please choose a Biblical name from the list.")
