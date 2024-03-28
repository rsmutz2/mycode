#!/usr/bin/env python3
"""Bible Memorization Tool - Python script that prompts the user to recite a Bible verse from memory and verifies if the recitation is correct"""


# Define the Bible verse to be memorized
bible_verse = "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. - John 3:16"

# Prompt the user to recite the Bible verse from memory
user_input = input("Please recite John 3:16 from memory: ")

# Verify if the user's recitation is correct
if user_input == bible_verse:
    print("Congratulations! You recited the verse correctly.")
elif user_input == "":
    print("Please provide a recitation.")
else:
    print("Incorrect recitation. Please try again.")
```

In this script, the user is prompted to recite the Bible verse "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. - John 3:16" from memory. The script then compares the user's input to the correct verse and provides feedback based on whether the recitation is correct
 or incorrect.

To further enhance this tool, you can add more Bible verses for memorization and create a loop that randomly selects
 a verse for the user to recite. You can also allow the user to keep trying until they recite the verse correctly.
