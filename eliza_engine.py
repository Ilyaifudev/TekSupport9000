import random

class Eliza:
    def __init__(self):
        self.rules = {}

    def load(self, filename):
        """
        Load rules from a file.
        Each line in the file should have the format:
        KEYWORD -> RESPONSE
        """
        with open(filename, 'r') as file:
            for line in file:
                if "->" in line:
                    keyword, response = line.strip().split("->")
                    self.rules[keyword.strip().lower()] = response.strip()

    def respond(self, user_input):
        """
        Generate a response based on user input.
        """
        user_input = user_input.lower()
        for keyword, response in self.rules.items():
            if keyword in user_input:
                return response
        return random.choice([
            "Can you tell me more?",
            "I'm here to help, please elaborate.",
            "Let's figure this out together. What seems to be the problem?"
        ])
