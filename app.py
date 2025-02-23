import streamlit as st
import random

# Initialize session state;

if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Streamlit App Layout;

st.title("🎯 Number Guessing Game 🔢")
st.write("Guess a number between 1 and 100!")


if not st.session_state.game_over:
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess")
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if user_guess < st.session_state.target_number:
            st.warning("⬆️ Too low! Try a higher number.")
        elif user_guess > st.session_state.target_number:
            st.warning("⬇️ Too high! Try a lower number.")
        else:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts! 🎊")
            st.session_state.game_over = True
else:
    if st.button("Play Again 🔄"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
