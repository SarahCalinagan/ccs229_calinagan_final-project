import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

def start_chat():
  """Starts a new chat session with the model."""
  chat = model.start_chat()
  return chat

def LLM_Response(chat, question):
  """Sends a message to the ongoing chat and returns the response."""
  response = chat.send_message(question, stream=True)
  return response

st.title("Detailed Exercise Challenge Creator")

# Create sidebar for prompts
with st.sidebar:
  st.header("Challenge Design")

  # Prompt 1: Goal Selection
  goal_selected = st.selectbox("What is your fitness goal?",
                              ("Build Muscle", "Lose Fat", "Improve Endurance", "Increase Flexibility"))

  # Prompt 2: Duration Selection
  duration_selected = st.selectbox("Challenge Duration", ("1 Week", "2 Weeks", "4 Weeks"))

  # Prompt 3 (Optional): Equipment Availability
  equipment_available = st.checkbox("Do you have access to gym equipment?")

  # Button to trigger challenge generation
  if st.button("Generate Challenge"):
    chat = start_chat()  # Start a new chat for each challenge
    challenge_prompt = f"Create a detailed {duration_selected} exercise challenge plan to help me achieve my goal of {goal_selected}."

    if equipment_available:
      challenge_prompt += " I have access to gym equipment."

    response = LLM_Response(chat, challenge_prompt)

    # Display the generated challenge plan (moved outside sidebar)
    st.subheader("Your Personalized Challenge:")
    for word in response:
      st.write(word.text)