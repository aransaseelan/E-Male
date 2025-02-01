import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Inject custom CSS to change the background color
st.markdown(
    """
    <style>
    /* Set the overall page background color */
    body {
        background-color: pink;
    }
    /* Optional: If you want to change the background of the main content container */
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load environment variables from a .env file if it exists
load_dotenv()

st.title("Manify Email")

# Try to get the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")

# If API key is not set, allow the user to input it securely
if not api_key:
    api_key = st.text_input("Enter your Google AI API key", type="password")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key  # Set the API key in the environment for later use

# Configure the API key if available
if api_key:
    genai.configure(api_key=api_key)

# Allow the user to input a prompt for the AI
user_prompt = st.text_area("Enter a prompt for content generation", "Explain how AI works")

# When the user clicks the button, generate content using the provided prompt
if st.button("Generate"):
    if not api_key:
        st.error("API key is required to generate content.")
    else:
        try:
            # Initialize the model (adjust the model name as needed)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_prompt)
            st.subheader("Generated Content")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
