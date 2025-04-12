import re
import random
import streamlit as st

# Common weak passwords
BLACKLIST = {"password", "12345678", "password123", "abcdefgh"}

# Scoring weights (you can tweak these)
WEIGHTS = {
    "length": 1.5,
    "uppercase": 1,
    "lowercase": 1,
    "digit": 0.5,
    "special": 1
}

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in BLACKLIST:
        feedback.append("This password is too common. Please choose something unique.")
        return 0, feedback

    # Length
    if len(password) >= 8:
        score += WEIGHTS["length"]
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += WEIGHTS["uppercase"]
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += WEIGHTS["lowercase"]
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit
    if re.search(r"\d", password):
        score += WEIGHTS["digit"]
    else:
        feedback.append("Add at least one number (0-9).")

    # Special char
    if re.search(r"[!@#$%^&*]", password):
        score += WEIGHTS["special"]
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return round(score, 2), feedback

def generate_strong_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit App
st.title("Password Strength Meter")

tab1, tab2 = st.tabs(["Check Password", "Generate Strong Password"])

with tab1:
    password = st.text_input("Enter your password", type="password")
    check_button = st.button("Check Password Strength")

    if password:
        score, feedback = check_password_strength(password)
        st.subheader(f"Score: {score} / 5")

        if score >= 4.5:
            st.success("✅ Strong Password!")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Consider strengthening it.")
        else:
            st.error("❌ Weak Password - Improve it using the tips below.")

        if feedback:
            st.markdown("**Suggestions:**")
            for tip in feedback:
                st.write("- " + tip)

with tab2:
    length = st.slider("Password Length", 8, 24, 12)
    if st.button("Generate Password"):
        new_password = generate_strong_password(length)
        
        st.success("Strong password generated!")
        st.code(new_password, language="text")
