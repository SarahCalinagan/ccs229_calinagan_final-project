import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Start a chat session
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    result = ""
    for word in response:
        result += word.text
    return result

def generate_exercise_challenge(difficulty, goal, duration, exercise_types, equipment, constraints):
    initial_prompt = f"Create a {difficulty} exercise challenge plan aimed at {goal} over {duration}. "
    initial_prompt += f"Include exercises like {exercise_types} and make use of {equipment}. "
    if constraints:
        initial_prompt += f"Consider the following constraints or preferences: {constraints}."
    detailed_plan = LLM_Response(initial_prompt)
    return detailed_plan

st.title("Exercise Challenge Creator")
st.markdown("Sarah Nicole D. Calinagan - **BSCS 3B AI**")

with st.sidebar:
    st.markdown("Let's create your Exercise Plan;\
            :sports_medal:")

    difficulty = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("Enter Your Fitness Goal (e.g., weight loss, muscle gain, endurance)")
    duration = st.selectbox("Select Challenge Duration", ["1 week", "2 weeks", "3 weeks", "1 month", "2 months", "3 months"])
    exercise_types = st.text_input("Preferred Types of Exercises (e.g., cardio, strength training, yoga)")
    equipment = st.text_input("Available Equipments")
    constraints = st.text_area("Constraints or Preferences")

    generate_btn = st.button("Submit")

if generate_btn and goal:
    with st.spinner("Please wait as we create your exercise plan..."):
        exercise_plan = generate_exercise_challenge(difficulty, goal, duration, exercise_types, equipment, constraints)
        st.subheader("Your Custom Exercise Challenge Plan")
        st.write(exercise_plan)