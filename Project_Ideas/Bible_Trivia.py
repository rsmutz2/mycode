#!/usr/bin/env python3
"""Bible Trivia Game! | Script prompts user to choose from 3 categories: Person, Place, or Thing. Then prompts the user to choose an item from the list, which then randomly prints up to 3 interesting facts about the item selected."""



import random

# Function that prints a random fact about the selected Bible character in the dictionary below.
def print_person_fact(character):
    facts = {
        "Abraham": ["Abraham is known as the father of many nations.", "Abraham and his wife Sarah had a son named Isaac in their old age.", "Abraham was called to sacrifice his son Isaac as a test of faith."],
        "Moses": ["Moses led the Israelites out of slavery in Egypt.", "Moses received the Ten Commandments from God on Mount Sinai.", "Moses spoke to God through a burning bush."],
        "David": ["David defeated Goliath with a sling and a stone.", "David became king of Israel after Saul.", "David wrote many of the Psalms in the Bible."],
        "Esther": ["Esther became queen of Persia and saved the Jewish people from a plot to destroy them.", "Esther's Hebrew name is Hadassah.", "Esther fasted for three days before approaching the king to save her people."],
        "Paul": ["Paul was originally known as Saul and persecuted early Christians.", "Paul had a dramatic conversion experience on the road to Damascus.", "Paul wrote many of the letters in the New Testament."],
        "Peter": ["Peter was one of Jesus' twelve disciples.", "Peter denied Jesus three times before the rooster crowed.", "Peter was a fisherman before becoming a follower of Jesus."],
        "Mary": ["Mary was the mother of Jesus.", "Mary received a visit from an angel announcing she would give birth to Jesus.", "Mary was present at the crucifixion and resurrection of Jesus."],
        "John": ["John was the disciple whom Jesus loved.", "John wrote the Gospel of John, three letters, and the book of Revelation in the Bible.", "John was exiled to the island of Patmos where he received the visions recorded in Revelation."],
        "Ruth": ["Ruth was a Moabite woman who became the great-grandmother of King David.", "Ruth's loyalty to her mother-in-law Naomi is a central theme in the book of Ruth.", "Ruth gleaned in the fields of Boaz, who later became her husband."],
        "Samson": ["Samson was known for his great strength.", "Samson's strength was in his hair, which was cut by Delilah.", "Samson killed many Philistines before his own death."]
    }
    fact = random.choice(facts[character])
    print(fact)

# Function that prints a random fact about the selected Biblical place in the dictionary below.
def print_place_fact(place):
    facts = {
        "Jerusalem": ["Jerusalem is considered a holy city by three major world religions: Judaism, Christianity, and Islam.", "Jerusalem is mentioned over 800 times in the Bible.", "Jerusalem was captured and recaptured over 40 times in its history."],
        "Bethlehem": ["Bethlehem is the birthplace of Jesus.", "Bethlehem means 'House of Bread' in Hebrew.", "Bethlehem is located in the West Bank, about 6 miles south of Jerusalem."],
        "Egypt": ["Egypt is where the Israelites were enslaved before their exodus led by Moses.", "Egypt is mentioned over 600 times in the Bible.", "Egypt is located in North Africa and is known for its ancient civilization."],
        "Mount Sinai": ["Mount Sinai is where Moses received the Ten Commandments from God.", "Mount Sinai is also known as Mount Horeb in the Bible.", "Mount Sinai is located in the Sinai Peninsula in Egypt."],
        "Babylon": ["Babylon is known for the hanging gardens, one of the Seven Wonders of the World.", "Babylon is mentioned in the Bible as a symbol of evil and rebellion against God.", "Babylon was a powerful ancient city located in present-day Iraq."],
        "Nineveh": ["Nineveh was the capital of the ancient Assyrian Empire.", "Nineveh was known for its great size and wealth.", "Nineveh is mentioned in the Bible as a city that repented after the preaching of Jonah."]
    }
    fact = random.choice(facts[place])
    print(fact)

# Function that prints a random fact about the Biblical thing in the dictionary below.
def print_thing_fact(thing):
    facts = {
        "Ark of the Covenant": ["The Ark of the Covenant contained the tablets of the Ten Commandments.", "The Ark of the Covenant was carried by the Israelites during their wanderings in the wilderness.", "Touching the Ark of the Covenant was forbidden and resulted in death."],
        "Manna": ["Manna was the bread-like substance that God provided for the Israelites in the wilderness.", "Manna was described as tasting like honey.", "Manna ceased to fall when the Israelites entered the Promised Land."],
        "Serpent Staff": ["Moses used a serpent staff to perform miracles before Pharaoh.", "The serpent staff was used to heal the Israelites from snakebites in the wilderness.", "The serpent staff was a symbol of God's power and authority."],
        "Goliath's Armor": ["Goliath's armor was made of bronze and weighed 125 pounds.", "Goliath's helmet alone weighed 15 pounds.", "David chose not to wear Goliath's armor when facing him in battle."],
        "Tabernacle": ["The Tabernacle was a portable sanctuary used by the Israelites in the wilderness.", "The Tabernacle housed the Ark of the Covenant and other sacred items.", "The design and construction of the Tabernacle is described in detail in the book of Exodus."],
        "Shepherd's Staff": ["The Shepherd's Staff was a symbol of David's humble beginnings as a shepherd.", "The Shepherd's Staff was used to guide and protect the sheep.", "The Shepherd's Staff is a symbol of God's care and provision."]
    }
    fact = random.choice(facts[thing])
    print(fact)

# Function that prints Welcome message and prompts user for input/category selection.
def main_menu():
    print("\nWelcome to the Bible Trivia Game!")
    print("Select a category:")
    print("1. Person")
    print("2. Place")
    print("3. Thing")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        person_menu()
    elif choice == '2':
        place_menu()
    elif choice == '3':
        thing_menu()
    elif choice == '4':
        print("\nThank you for playing the Bible Trivia Game!")
    else:
        print("\nInvalid choice. Please try again.")
        main_menu()

# Function that prints Character menu and prompts user for selection.
def person_menu():
    characters = ["Abraham", "Moses", "David", "Esther", "Paul", "Peter", "Mary", "John", "Ruth", "Samson"]
    
    print("\nSelect a Bible character:")
    for i, character in enumerate(characters, 1):
        print(str(i) + ". " + character)
    
    selection = input("Enter your choice (1-10): ")
    if selection.isdigit() and 1 <= int(selection) <= 10:
        character = characters[int(selection) - 1]
        print_person_fact(character)
        another = input("Would you like to select another character? (yes/no): ")
        if another.lower() == "yes":
            person_menu()
        else:
            main_menu()
    else:
        print("\nInvalid selection. Please try again.")
        person_menu()

# Function that prints Place menu and prompts user for selection.
def place_menu():
    places = ["Jerusalem", "Bethlehem", "Egypt", "Mount Sinai", "Babylon", "Nineveh"]
    
    print("\nSelect a place in the Bible:")
    for i, place in enumerate(places, 1):
        print(str(i) + ". " + place)
    
    selection = input("Enter your choice (1-6): ")
    if selection.isdigit() and 1 <= int(selection) <= 6:
        place = places[int(selection) - 1]
        print_place_fact(place)
        another = input("Would you like to select another place? (yes/no): ")
        if another.lower() == "yes":
            place_menu()
        else:
            main_menu()
    else:
        print("\nInvalid selection. Please try again.")
        place_menu()

# Function that prints Thing menu and prompts user for selection.
def thing_menu():
    things = ["Ark of the Covenant", "Manna", "Serpent Staff", "Goliath's Armor", "Tabernacle", "Shepherd's Staff"]
    
    print("\nSelect a thing from the Bible:")
    for i, thing in enumerate(things, 1):
        print(str(i) + ". " + thing)
    
    selection = input("Enter your choice (1-6): ")
    if selection.isdigit() and 1 <= int(selection) <= 6:
        thing = things[int(selection) - 1]
        print_thing_fact(thing)
        another = input("Would you like to select another thing? (yes/no): ")
        if another.lower() == "yes":
            thing_menu()
        else:
            main_menu()
    else:
        print("\nInvalid selection. Please try again.")
        thing_menu()

# Starts the program at the main menu
main_menu()
