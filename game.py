import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# UI
st.title("🎯 Number Guessing Game")
st.write("Guess the number between **1 and 100**")

st.write(f"### Attempts: {st.session_state.attempts}")

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1
)

# Game logic
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Try a higher number 📈")

    elif guess > st.session_state.number:
        st.warning("Try a lower number 📉")

    else:
        st.success(
            f"🎉 Correct! The number was {st.session_state.number}"
        )
        st.session_state.game_over = True

# Restart
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()
