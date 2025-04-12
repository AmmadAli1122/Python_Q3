
# 🔐 Password Strength Meter with Generator

A **Streamlit web app** that checks the strength of your password and helps you create secure ones. It uses customizable rules to evaluate and generate passwords, ensuring better online security.

---

## 🚀 Features

- ✅ **Password Strength Checker**  
  Analyze your password based on:
  - Minimum length (8+ characters)
  - Use of uppercase & lowercase letters
  - Digits and special characters
  - Custom scoring weights
  - Blacklist detection for common passwords

- 🔁 **Strong Password Generator**  
  Generate random secure passwords with a copy button.

- 🖥️ **User Interface with Streamlit**  
  - Two tabs: Check password strength & generate password
  - Copy button for easy use
  - Instant feedback & tips for improvement

---

## 📦 Requirements

- Python 3.x
- Streamlit

Install dependencies with:

```bash
pip install streamlit
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

(Replace `app.py` with your actual filename if different.)

---

## 🧠 How It Works

### ✅ Scoring Criteria:
| Criteria              | Points |
|-----------------------|--------|
| Length ≥ 8            | 1.5    |
| Uppercase letter      | 1      |
| Lowercase letter      | 1      |
| Number (0-9)          | 0.5    |
| Special character     | 1      |
| **Max Score**         | **5**  |

> Common weak passwords like `"password123"` are blocked even if they meet other rules.

---

## ✨ Example

**Password:** `Hello123!`  
**Score:** `4.5 / 5`  
**Status:** ✅ Strong Password!


