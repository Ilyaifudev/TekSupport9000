from eliza import Eliza

# Initialize and load rules
bot = Eliza()
bot.load("rules.txt")

# Test conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Eliza: Goodbye!")
        break
    response = bot.respond(user_input)
    print(f"Eliza: {response}")
