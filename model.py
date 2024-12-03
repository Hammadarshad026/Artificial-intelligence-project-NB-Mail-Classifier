import pickle
import pyfiglet
from termcolor import colored
from text_formater import reformat_text

import os 
os.system('cls')
# Create the ASCII art
ascii_art = pyfiglet.figlet_format("HAMMAD")
colored_art = colored(ascii_art, color="blue", attrs=["bold", "blink"])

# Display the banner
print(colored("This program is written  by:", color="green", attrs=["bold"]))
print(colored_art)



with open("trained_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)

input_text=input("Enter mail here> ")
user=reformat_text(input_text)
new_messages = [user]

new_messages_vec = loaded_vectorizer.transform(new_messages)


predictions = loaded_model.predict(new_messages_vec)
if predictions[0] == 1 :
        # Create the ASCII art
    ascii_art = pyfiglet.figlet_format("HAM")
    colored_art = colored(ascii_art, color="green", attrs=["bold", "blink"])

    # Display the banner
    print(colored_art)
    print(colored("Delicious and not spam!", color="yellow", attrs=["bold", "underline"]))
else :
    # Create the banner
    ascii_art = pyfiglet.figlet_format("SPAM")
    colored_art = colored(ascii_art, color="red", attrs=["bold", "blink"])

    # Display the banner
    print(colored_art)
    print(colored("Warning: This is a spam message!", color="yellow", attrs=["bold", "underline"]))