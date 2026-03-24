import streamlit as st
import whisper
import os
from PIL import Image

# 1. App Configuration & Premium Theme
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# Custom CSS for English Interface & Centering
st.markdown("""
    <style>
    /* Background & Global Text */
    .main { background-color: #0e1117; color: white; }
    
    /* Centering Image & Title */
    .header-container {
        text-align: center;
        padding: 50px 0px 20px 0px;
    }
    
    .profile-img {
        width: 220px;
        height: 220px;
        border-radius: 20px; /* Square with rounded corners as per your photo style */
        object-fit: cover;
        border: 4px solid #FF4B4B;
        margin-bottom: 20px;
    }
    
    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 48px;
        color: #ffffff;
        margin: 0;
    }
    
    .sub-title {
        font-size: 18px;
        color: #8b949e;
        margin-bottom: 40px;
    }
    
    /* Button Design */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #FF4B4B, #FF1F1F);
        color: white;
        height: 3.5em;
        font-weight: bold;
        font-size: 18px;
        border: none;
    }
    
    /* Result Box Style */
    .result-box {
        background-color: #1a1c24;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Centered Photo and Title (English)
st.markdown('<div class="header-container">', unsafe_allow_html=True)

try:
    # Displaying your photo first
    img = Image.open("my_photo.jpg.jpeg")
    st.image(img, width=220) # This will be centered automatically by Streamlit in this context
except:
    st.info("📸 Logo loading...")

st.markdown('<h1 class="main-title">Solaiman Transcript & SEO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your AI-powered tool for Video Transcription & SEO Automation</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 3. Video Upload Section (English)
uploaded_file = st.file_uploader("📂 Upload or Drop your video file here (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("Generate SEO Content ✨"):
        with st.spinner('Processing... Please wait, Solaiman! AI is analyzing your video.'):
            # Save temporary video
            with open("temp_vid.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # 4. Transcription Logic (Whisper AI)
            model = whisper.load_model("base")
            result = model.transcribe("temp_vid.mp4")
            transcript_text = result['text']
            
            # 5. Result Display (English UI)
            st.success("Success! Your content is ready.")
            
            st.markdown("### 📌 1. Engaging Video Title")
            st.code(f"Viral Video: {transcript_text[:60]}... 🔥")
            
            st.markdown("### 📝 2. Full Bengali Transcript")
            st.text_area("Transcri
