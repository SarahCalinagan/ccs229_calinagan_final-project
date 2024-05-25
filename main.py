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

def generate_exercise_challenge(difficulty, goal, duration):
    initial_prompt = f"Create a {difficulty} exercise challenge plan aimed at {goal} over {duration}."
    detailed_plan = LLM_Response(initial_prompt)
    return detailed_plan

st.title("Detailed Exercise Challenge Creator")

with st.sidebar:
    st.header("Customize Your Exercise Challenge")

    difficulty = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("Enter Your Fitness Goal (e.g., weight loss, muscle gain, endurance)")
    duration = st.selectbox("Select Challenge Duration", ["1 week", "2 weeks", "1 month", "3 months"])

    generate_btn = st.button("Generate Exercise Plan")

if generate_btn and goal:
    with st.spinner("Generating your exercise plan..."):
        exercise_plan = generate_exercise_challenge(difficulty, goal, duration)
        st.subheader("Your Custom Exercise Challenge Plan")
        st.write(exercise_plan)