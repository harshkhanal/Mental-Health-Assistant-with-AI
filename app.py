import streamlit as st
from chatbot import chatbot_response

# Streamlit page configuration
st.set_page_config(page_title="AI Mental Health Chatbot", layout="centered")

# Title and description
st.title("AI Mental Health Chatbot")
st.write("Welcome! I'm here to help. Ask me anything, and I'll do my best to assist you.")

# Create a text input box for the user to chat
user_input = st.text_input("Type your question or share how you're feeling:")

# Display the chatbot response
if user_input:
    response = chatbot_response(user_input)
    st.write(f"Bot: {response}")
