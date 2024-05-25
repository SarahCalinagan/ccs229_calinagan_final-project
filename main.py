import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=st.secrets["GOOGLE_GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')


def multi_level_prompt():
    """
    Gathers user input from the sidebar for vacation itinerary prompts.

    Returns:
        tuple: User-entered destination, duration, and activities.
    """

    with st.sidebar:
        # Destination prompt
        destination = st.text_input("Enter your vacation destination:")

        # Duration prompt
        duration = st.number_input("Enter the duration of your stay (in days):", min_value=1, max_value=365)

        # Activities prompt (multiselect)
        activities = st.multiselect("Select your interests and activities:",
                                   ["Adventure", "Relaxation", "Culture", "Nature", "Food", "Shopping"])

    return destination, duration, activities


def generate_itinerary(destination, duration, activities):
    """
    Generates a vacation itinerary based on user-provided prompts.

    Args:
        destination (str): User-entered vacation destination.
        duration (int): User-entered duration of stay (days).
        activities (list): User-selected list of activities.

    Returns:
        str: Generated vacation itinerary text.
    """

    activities_str = ", ".join(activities)
    prompt = f"Create a {duration}-day vacation itinerary for {destination} with a focus on {activities_str}."
    print(prompt)  # This line is added for debugging

    # Generate response using the Gemini-Pro model
    response = model.generate_text(prompt=prompt)
    return response['generated_text']


def main():
    """
    Main function that runs the Streamlit app for vacation itinerary generation.
    """

    # Multi-level prompting for user input in sidebar
    destination, duration, activities = multi_level_prompt()

    # Generate button and display generated itinerary
    if st.button("Generate Itinerary"):
        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(destination, duration, activities)
        st.success("Here's your vacation itinerary:")
        st.write(itinerary)


if __name__ == "__main__":
    main()
