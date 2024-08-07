import streamlit as st
from flowise_integration.py import get_flowise_response

# Set up the Streamlit app
st.title("Weather Chatbot")
st.write("Ask about the weather conditions for specific places.")

# User input
user_input = st.text_input("You: ", "")

if user_input:
    # Get response from FlowiseAI
    response = get_flowise_response(user_input)
    
    # Display the response
    st.write(f"Chatbot: {response}")
