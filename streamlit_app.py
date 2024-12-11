import streamlit as st
from eliza import Eliza  # Ensure Eliza is in the same directory

# Initialize Eliza bot
eliza_bot = Eliza()
eliza_bot.load('rules.txt')  # Load the customized rules file

# Set up the Streamlit app
st.title("Tech Support Chatbot")
st.write("Hello! I'm your tech support assistant. How can I help you today?")

# User input
user_input = st.text_input("Describe your issue:")

# Respond using Eliza
if user_input:
    response = eliza_bot.respond(user_input)
    st.write(f"**Tech Support:** {response}")

# Display common issues
st.write("#### Example Issues You Can Ask About:")
examples = [
    "My computer is slow",
    "The internet is not working",
    "Printer not responding",
    "How can I fix a blue screen of death?",
    "What should I do if my computer overheats?"
]
for example in examples:
    st.write(f"- {example}")

