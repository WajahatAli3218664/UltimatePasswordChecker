import streamlit as st
import re
import random
import string
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to load Lottie animation from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading Lottie animation: {e}")
        return None

# Load Lottie animations
lottie_animation = load_lottieurl("https://raw.githubusercontent.com/WajahatAli3218664/cv-generator/refs/heads/main/Animation%20-%201741472475576.json")  # Main animation
lottie_heading = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qp1q7mct.json")  # Heading animation

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }
    /* Purple button styling matching the screenshot */
    .stButton>button {
        background-color: #6200EA !important;
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #5000D0 !important;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h2 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h3 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    /* Ensure Lottie animation is visible in both light and dark themes */
    .lottie-container {
        background-color: transparent;
    }
    /* Amazing Footer Styling */
    .amazing-footer {
        width: 100%;
        padding: 20px;
        margin-top: 30px;
        border-radius: 8px;
        background: linear-gradient(135deg, #273c75 0%, #192a56 100%);
        color: white;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        animation: fadeIn 1.5s ease-in-out;
    }
    .footer-quote {
        font-style: italic;
        font-size: 18px;
        margin-bottom: 15px;
        color: #f5f6fa;
    }
    .designer-credit {
        font-weight: bold;
        color: #fbc531;
        font-size: 16px;
    }
    /* Password Strength Meter */
    .password-strength-meter {
        width: 100%;
        height: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin-top: 10px;
        overflow: hidden;
    }
    .password-strength-meter-fill {
        height: 100%;
        transition: width 0.5s ease-in-out;
    }
    .strength-0 { background-color: #ff5252; width: 25%; }
    .strength-1 { background-color: #ff5252; width: 50%; }
    .strength-2 { background-color: #ffd740; width: 75%; }
    .strength-3 { background-color: #69f0ae; width: 100%; }
    /* Responsive adjustments for mobile view */
    @media (max-width: 768px) {
        .stMarkdown h1 {
            font-size: 24px;
        }
        .stMarkdown h2 {
            font-size: 20px;
        }
        .stMarkdown h3 {
            font-size: 18px;
        }
        .stTextInput>div>div>input {
            font-size: 14px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px 16px;
        }
        .lottie-container {
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App
def main():
    # Title with Lottie Animation
    col1, col2 = st.columns([1, 2])
    with col1:
        if lottie_heading:
            st_lottie(lottie_heading, height=100, key="heading")
    with col2:
        st.title("🔐 Ultimate Password Strength Checker")

    # Description with Animation
    st.markdown(
        """
        <div class="fadeIn">
            <p>Welcome to the <strong>Ultimate Password Strength Checker!</strong>  
            Ensure your password is secure by checking:</p>
            <ul>
                <li>✅ Length</li>
                <li>✅ Upper & Lowercase letters</li>
                <li>✅ Numbers</li>
                <li>✅ Special Characters</li>
            </ul>
            <blockquote>⚡ <em>Improve your online security by creating strong passwords!</em></blockquote>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input Field
    password = st.text_input("🔑 Enter your password:", type="password")

    # Password Strength Meter
    if password:
        score, _ = check_password_strength(password)
        st.markdown(f'<div class="password-strength-meter"><div class="password-strength-meter-fill strength-{score}"></div></div>', unsafe_allow_html=True)

    # Button to Check Password - now with purple color
    if st.button("🔍 Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)

            st.subheader("🔒 Password Strength Result:")

            if score == 4:
                st.success("✅ Strong Password! Your password is secure.", icon="🎉")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.", icon="⚠️")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below.", icon="🚨")

            if feedback:
                st.info("💡 Suggestions to improve your password:")
                for tip in feedback:
                    st.write(tip)
        else:
            st.error("🚨 Please enter a password to check.")

    # Password Generator Section
    st.markdown("---")
    st.subheader("🔧 Password Generator")
    password_length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        generated_password = generate_password(password_length)
        st.success(f"🔐 Generated Password: `{generated_password}`")

    # Ensure Lottie Animation is always rendered
    if lottie_animation:
        st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
        st_lottie(lottie_animation, height=300, key="animation")
        st.markdown('</div>', unsafe_allow_html=True)

    # Amazing Footer with Animation
    st.markdown(
        """
        <div class="amazing-footer">
            <p class="footer-quote">"Our greatest glory is not in never falling, but in rising every time we fall."</p>
            <p class="designer-credit">Designed by Wajahat Ali</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Run the app
if __name__ == "__main__":
    main()
