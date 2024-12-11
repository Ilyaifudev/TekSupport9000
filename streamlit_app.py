import streamlit as st
from eliza_engine import Eliza  # Import the Eliza class from eliza_engine.py

# Initialize Eliza bot
eliza_bot = Eliza()
eliza_bot.load('rules.txt')  # Load tech support rules from rules.txt

# Streamlit interface
st.title("Tech Support AI Agent")
st.write("Welcome! I'm your tech support assistant. How can I help you today?")

# User Input
user_query = st.text_input("Describe your issue:", "")

# Process User Input
if user_query:
    response = eliza_bot.respond(user_query)
    st.write(f"**Tech Support:** {response}")

# Example Quick Questions
st.write("#### Common Issues You Can Ask About:")
examples = [
    "My computer is slow",
    "The internet is not working",
    "Printer not responding",
    "How can I fix overheating?",
    "Why is my sound not working?"
]
for example in examples:
    st.write(f"- {example}")
