# Ask the question
COUNTRY = input("what is the capital of France?")

# Check if answer is correct
if COUNTRY.strip().lower() == "paris":
    print("the answer is correct.")
else:
    print("the answer is wrong.")