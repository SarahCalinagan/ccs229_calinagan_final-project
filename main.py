import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

def generate_challenge(prompt):
        """
        Generates an exercise challenge plan based on the provided prompt.
        """
        try:
            response = model.generate(prompt=prompt)
            return response.text()
        except Exception as e:
            st.error(f"Error generating challenge: {e}")
            return None

st.title("Exercise Challenge Creator")

# Sidebar for user input
with st.sidebar:
  st.header("Challenge Details")
  focus_area = st.selectbox("Focus Area", ["Cardio", "Strength Training", "Flexibility"])
  duration = st.number_input("Duration (Weeks)", min_value=1)
  frequency = st.radio("Frequency", ("Daily", "Weekly"))
  difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])
  additional_info = st.text_area("Additional Information (Optional)")

  # Combine user input into a prompt
  prompt = f"Create a detailed {duration}-week {frequency} {focus_area} exercise challenge plan for a {difficulty} level. "
  if additional_info:
    prompt += f" Additional considerations: {additional_info}"

  # Generate challenge plan
  if st.button("Generate Challenge"):
    challenge_plan = generate_challenge(prompt)
    st.write("## Challenge Plan:")
    st.text(challenge_plan)
