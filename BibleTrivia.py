#!/usr/bin/env python3
"""Bible Trivia"""


# Create a dictionary of Bible verses with their corresponding chapters and verses
bible_verses = {
    "John 3:16": "For God so loved the world that he gave his only begotten Son, that whosever believeth in him should not perish but have everlasting life.",
    "Philippians 4:13": "I can do all things through Christ who strengtheneth me.",
    "Psalm 23:1": "The Lord is my shepherd, I shall not want.",
}

# Function to display the trivia question and check the answer
def trivia_game():
    print("Welcome to the Bible Verse Trivia Game!")
    verse = input("Guess the Bible verse: ")

    if verse in bible_verses:
        print("Correct! The verse is:", bible_verses[verse])
    else:
        print("Incorrect. Try again!")

# Play the game
trivia_game()
