import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')


# Sidebar for User Input
st.sidebar.header("Exercise Challenge Creator")

# Prompt Levels (Modify these based on your desired challenge structure)
prompt_levels = {
    "Level 1": "What type of exercise will this challenge focus on (e.g., strength, cardio, flexibility)?",
    "Level 2": "How long will this challenge last (e.g., 1 week, 30 days)?",
    "Level 3": "What is the overall difficulty level (e.g., beginner, intermediate, advanced)?",
    "Level 4": "Describe any specific equipment needed (e.g., weights, yoga mat, none)?",
}

# Current Level (starts at 1)
current_level = 1

# Loop through Prompt Levels
while current_level <= len(prompt_levels):
    # Display Current Level Prompt
    user_input = st.sidebar.text_input(prompt_levels[f"Level {current_level}"])

    # Check for User Input
    if user_input:
        # Generate Prompt based on Level and User Input
        prompt = f"Create a detailed daily exercise challenge that focuses on {user_input}."

        # Call Google Generative AI and Generate Challenge Description
        try:
            response = model.generate(prompt=prompt)
            generated_text = response.texts[0]
            st.success(f"Level {current_level} Complete!")
            st.write(generated_text)
        except Exception as e:
            st.error(f"Error generating text: {e}")

        # Increment Level
        current_level += 1
        # Clear User Input after successful generation
        st.sidebar.text_input("", value=user_input, key=f"temp-{current_level}")
    else:
        st.write("Please enter your input for the current prompt.")

# Display Completion Message if all Levels Completed
if current_level > len(prompt_levels):
    st.success("Your detailed exercise challenge is complete!")