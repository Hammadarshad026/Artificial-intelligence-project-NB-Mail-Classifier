def reformat_text(input_text):
    lines = input_text.strip().splitlines()
    reformatted_text = " ".join(line.strip() for line in lines if line.strip())
    reformatted_text = reformatted_text.replace(". ", ".").replace(".", ". ")
    reformatted_text = " ".join(reformatted_text.split()) 
    return reformatted_text

# # Input text
# input_text = """MAKE MONEY FAST!!!
# Click this link to claim your FREE gift: https://www.sotwe.com/fakecurrency

# You've been selected for a limited-time offer! Don't miss out!

# Best, [Hammad]"

# This text contains common spam triggers, such as:

# - All caps and excessive punctuation
# - Promises of easy money or gifts
# - Suspicious links
# - Urgency tactics (limited-time offer)
# - Fake or generic sender names

# AI-powered spam filters would likely flag this email as spam due to these red flags."""

# # Reformatted output
# output_text = reformat_text(input_text)
# print(output_text)
