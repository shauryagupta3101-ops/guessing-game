import streamlit as st
import random
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# ---------------- CSS UI ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1d2671, #c33764);
}
.main {
    background: rgba(255,255,255,0.15);
    padding: 25px;
    border-radius: 20px;
}
h1, h2, h3 {
    text-align: center;
    color: white;
}
.info-box {
    background: rgba(255,255,255,0.2);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SOUND FUNCTIONS ----------------
def play_sound(file):
    with open(file, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}">
            </audio>
            """,
            unsafe_allow_html=True,
        )

# ---------------- SESSION STATE ----------------
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# ---------------- UI ----------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("🎯 Number Guessing Game")
st.write("### Guess the number between **1 and 100**")

st.markdown(
    f"<div class='info-box'>Attempts: {st.session_state.attempts}</div>",
    unsafe_allow_html=True
)

guess = st.number_input(
    "Enter your guess 👇",
    min_value=1,
    max_value=100,
    step=1
)

# ---------------- GAME LOGIC ----------------
if st.button("🎯 Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("📈 Try a **higher** number")
        play_sound("wrong.mp3")

    elif guess > st.session_state.number:
        st.warning("📉 Try a **lower** number")
        play_sound("wrong.mp3")

    else:
        st.success(f"🎉 You caught me! The number was **{st.session_state.number}**")
        st.balloons()
        play_sound("win.mp3")
        st.session_state.game_over = True

# ---------------- RESTART ----------------
if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
