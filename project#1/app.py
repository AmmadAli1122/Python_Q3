import streamlit as st
import random
import datetime

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# Title
st.title("🌱 Growth Mindset Challenge")
st.subheader("Develop your abilities through effort and learning!")

# Motivational Quotes
quotes = [
    "Your brain is like a muscle. The more you use it, the stronger it gets!",
    "Mistakes are proof that you are trying.",
    "Challenges make you stronger. Embrace them!",
    "Effort and persistence lead to mastery.",
    "The only limit to your learning is your mindset."
]
st.info(random.choice(quotes))

# Daily Challenge Generator
challenges = [
    "Write down 3 things you learned from a mistake.",
    "Teach a new concept to someone else.",
    "Take on a difficult task and break it into small steps.",
    "Find a success story that inspires you and write about it.",
    "Practice positive self-talk for the entire day!"
]
today = datetime.date.today()
random.seed(today.toordinal()) 
st.subheader("🔥 Today's Challenge:")
st.write(f"👉 {random.choice(challenges)}")

# Reflection Section
st.subheader("📝 Reflect on Your Learning")
with st.form("reflection_form"):
    progress = st.text_area("What progress have you made towards your learning goals?")
    biggest_challenge = st.text_area("What was your biggest challenge today?")
    improvement = st.text_area("How will you improve tomorrow?")
    submitted = st.form_submit_button("Submit Reflection")

    if submitted:
        st.success("Your are doing great! Keep growing! 🌟")

# Footer
st.markdown("---")
st.write("🚀 Thank You..!")

