import streamlit as st
from eliza_engine import Eliza  # Ensure this imports correctly

# Function to Add Custom Background
def add_custom_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.ibb.co/h1CpXg0/peakpx.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add the custom background
add_custom_background()

# Initialize Eliza bot
eliza_bot = Eliza()
eliza_bot.load('rules.txt')  # Load tech support rules from rules.txt

# Streamlit Interface
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
