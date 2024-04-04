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
      facts = ["Adam was the first human God created.",
               "Adam and his wife, Eve, were the very first couple in the Bible.",
               "God formed Adam from the dust of the ground, who then lived 930 years before returning to the dust.",
               "By the sin of the '1st Adam' came death upon all humanity; but by the obedience of the '2nd Adam' (that is, Jesus Christ), came grace and life unto all.",
               "Adam gave names to all cattle, to all the fowl of the air, and to every beast of the field."]
    elif user_choice == "Eve":
      facts = ["Eve was the first woman God created.",
               "Adam named his wife Eve because she was the mother of all living.",
               "Adam called Eve 'woman' because she was taken out of man (God formed her from Adam's rib)",
               "Eve was tempted by the serpent to eat the fruit God commanded her not to eat."]
    elif user_choice == "Moses":
      facts = ["Moses was a Hebrew prophet who led the Israelites out of bondage and slavery in Egypt.",
               "Moses received the Ten Commandments written with the finger of God on Mount Sinai.",
               "Moses wrote the first five books of the Bible, known as the Torah.",
               "Moses was called the meekest man upon the face of the earth.",
               "Moses was a great man of prayer. When God's anger burned toward the people for their sin, Moses stood in the gap, turning the fiercesome wrath of God away."]
    elif user_choice == "Sarah":
      facts = ["Sarah was the wife of Abraham and mother of Isaac and Esau.",
               "Sarah gave birth to Isaac at the age of 90 years old!",
               "Sarah laughed when she heard she would have a son in her old age, leading to the naming of Isaac ('laughter').",
               "Sarah lived to be 127 years old.",
               "Sarah had been called Sarai before God himself changed it."]
    elif user_choice == "David":
      facts = ["David was the second king of Israel, next after Saul.",
               "David defeated the Philistine giant Goliath with a sling and a stone in the Valley of Elah.",
               "David wrote many of the Psalms of the Bible.",
               "David was called 'a man after God's own heart.",
               "David was 30 when he became King of Judah in Israel and reigned 40 years."]
    
    random_fact = random.choice(facts)
    
    print("Did you know?")
    print(random_fact)
else:
    print("Invalid choice. Please choose a Biblical name from the list.")
