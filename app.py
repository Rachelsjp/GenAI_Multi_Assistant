import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import assistants
from assistants import chat, sql, email, cover_letter, mock_interview, youtube

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Gen AI Assistant", layout="wide")

# ---------------------------------------------------
# DARK UI CSS (FINAL - STRONG OVERRIDES)
# ---------------------------------------------------
st.markdown("""
<style>

/* ===== REMOVE STREAMLIT HEADER ===== */
header {
    visibility: hidden;
}

/* ===== FULL BACKGROUND ===== */
html, body, [class*="css"] {
    background-color: #0B0F19 !important;
}

.stApp {
    background-color: #0B0F19;
}

/* ===== REMOVE TOP SPACE ===== */
section.main > div {
    padding-top: 0rem !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background-color: #11131A !important;
    padding: 20px;
}

section[data-testid="stSidebar"] * {
    color: #E6EAF0 !important;
}

/* ===== ALL TEXT WHITE ===== */
h1, h2, h3, h4, h5, h6,
p, div, label, span {
    color: #FFFFFF !important;
}

/* ===== INPUT BOXES ===== */
.stTextInput>div>div>input {
    background-color: #1A1D24 !important;
    color: white !important;
    border: 1px solid #2A2F3A !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* ===== TEXT AREA ===== */
textarea {
    background-color: #1A1D24 !important;
    color: white !important;
    border-radius: 10px !important;
}

/* ===== BUTTON ===== */
.stButton>button {
    background-color: #2E7D32 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px 18px !important;
    border: none !important;
}

.stButton>button:hover {
    background-color: #388E3C !important;
}

/* ===== DARK CODE BLOCK ===== */
pre, code {
    background-color: #1A1D24 !important;
    color: #FFFFFF !important;
}

/* ===== REMOVE WHITE BLOCK ===== */
.block-container {
    background-color: #0B0F19 !important;
}

/* ===================================================
   ✅ FILE UPLOADER FULL FIX (TEXT + ICON BLACK)
   =================================================== */
div[data-testid="stFileUploader"] {
    background-color: #EDEDED !important;
    border-radius: 12px;
    padding: 15px;
}

div[data-testid="stFileUploader"] * {
    color: #000000 !important;
}

div[data-testid="stFileUploader"] svg {
    fill: #000000 !important;
    color: #000000 !important;
}

/* ===================================================
   ✅ PLACEHOLDER TEXT FIX (MOCK INTERVIEW)
   =================================================== */
.stTextArea textarea::placeholder {
    color: #000000 !important;
    opacity: 1 !important;
}

.stTextInput input::placeholder {
    color: #000000 !important;
}

textarea::-webkit-input-placeholder {
    color: #000000 !important;
}

/* ===== FONT ===== */
* {
    font-family: "Segoe UI", sans-serif;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🧠 Assistants")

# ✅ Branding
st.sidebar.markdown(
    """
    <div style="margin-top:-8px; margin-bottom:15px;">
        <span style="color:#6C757D; font-size:12px;">
            Developed by
        </span><br>
        <span style="color:#FFFFFF; font-size:14px; font-weight:500;">
            Rachel Purnima Johnpeter
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

assistant = st.sidebar.radio(
    "",
    [
        "💬 Chat Assistant",
        "💻 SQL Assistant",
        "📧 Email Writer",
        "📄 Cover Letter Generator",
        "🎤 Mock Interview",
        "📺 YouTube Summarizer"
    ]
)

# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------
st.title("🚀 GEN AI ASSISTANT")

# ---------------------------------------------------
# ROUTING
# ---------------------------------------------------
if assistant == "💬 Chat Assistant":
    chat.run()

elif assistant == "💻 SQL Assistant":
    sql.run()

elif assistant == "📧 Email Writer":
    email.run()

elif assistant == "📄 Cover Letter Generator":
    cover_letter.run()

elif assistant == "🎤 Mock Interview":
    mock_interview.run()

elif assistant == "📺 YouTube Summarizer":
    youtube.run()