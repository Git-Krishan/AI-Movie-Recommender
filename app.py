import streamlit as st
import random

# Define moods
moods = ["happy", "sad", "excited", "romantic", "angry", "bored", "motivated", "tired", "anxious", "nostalgic"]

# Sample base movie titles
base_movies = [
    "Inception", "Forrest Gump", "The Matrix", "Titanic", "Interstellar",
    "The Dark Knight", "The Shawshank Redemption", "Pulp Fiction",
    "La La Land", "The Godfather", "Parasite", "Joker", "Avengers: Endgame"
]

# Generate 650+ movies per mood by repeating base list
movie_dict = {
    mood: [f"{movie} ({i+1})" for i in range(50) for movie in base_movies]
    for mood in moods
}

# Streamlit UI
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬")
st.title("🎬 Mood-Based Movie Recommender (Large List)")
st.write("Enter your current mood, and I'll suggest movies that match!")

# Input field
mood_input = st.text_input("What's your mood? (e.g., happy, sad, romantic, excited)").lower().strip()

if mood_input:
    if mood_input in movie_dict:
        st.success(f"Here are some movie recommendations for when you're feeling {mood_input}:")
        # Show random 10 from the large list
        recommended = random.sample(movie_dict[mood_input], 10)
        for movie in recommended:
            st.write("👉", movie)
    else:
        st.error("Sorry, I don't recognize that mood. Try one of these:")
        st.write(", ".join(moods))
