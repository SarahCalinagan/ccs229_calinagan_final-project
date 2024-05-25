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

# Define function for multi-level prompting
def multi_level_prompt():
    # Level 1 prompt
    destination = st.text_input("Enter your vacation destination:")
    
    # Level 2 prompt
    duration = st.number_input("Enter the duration of your stay (in days):", min_value=1, max_value=365)
    
    # Level 3 prompt
    activities = st.multiselect("Select your interests and activities:", ["Adventure", "Relaxation", "Culture", "Nature", "Food", "Shopping"])
    
    return destination, duration, activities

# Generate vacation itinerary based on prompts
def generate_itinerary(destination, duration, activities):
    # Create a prompt for the model
    activities_str = ", ".join(activities)
    prompt = f"Create a {duration}-day vacation itinerary for {destination} with a focus on {activities_str}."
    
    # Generate response using the Gemini-Pro model
    response = model.generate_text(prompt=prompt)
    return response['generated_text']

# Main function to run the app
def main():
    # Multi-level prompting
    destination, duration, activities = multi_level_prompt()
    
    # Generate vacation itinerary
    if st.button("Generate Itinerary"):
        # Display loading message
        with st.spinner("Generating itinerary..."):
            # Call function to generate itinerary
            itinerary = generate_itinerary(destination, duration, activities)
            # Display generated itinerary
            st.success("Here's your vacation itinerary:")
            st.write(itinerary)

if __name__ == "__main__":
    main()