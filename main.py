import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    return response

st.title("Creative Text Generator")

# Level 1 Prompt: Specify the Genre
st.header("Level 1: Specify the Genre")
genre_input = st.text_input("Enter a genre (e.g., Sci-Fi, Fantasy, Mystery):")

# Level 2 Prompt: Describe the Scene
st.header("Level 2: Describe the Scene")
scene_description = st.text_area("Describe the scene or scenario:")

# Level 3 Prompt: Introduce a Character
st.header("Level 3: Introduce a Character")
character_name = st.text_input("Enter the character's name:")
character_description = st.text_area("Describe the character:")

# Generate Text
btn = st.button("Generate")
if btn and genre_input and scene_description and character_name and character_description:
    prompt = f"In a {genre_input.lower()} setting, {scene_description}. "
    prompt += f"There was a character named {character_name} who {character_description}. "
    
    result = LLM_Response(prompt)
    
    # Display Response
    st.subheader("Generated Text:")
    for word in result:
        st.text(word.text)