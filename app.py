import streamlit as st
import whisper
import os
import base64
from PIL import Image

# 1. App Configuration
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# Function to load local image and convert to base64 for absolute centering
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- Custom Styling for Absolute Centering ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    
    /* Main container to hold everything in the center */
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding-top: 40px;
    }

    /* Image Styling */
    .profile-pic {
        width: 250px;
        height: 250px;
        border-radius: 15px; /* Rounded corners */
        border: 4px solid #FF4B4B;
        object-fit: cover;
        margin-bottom: 20px;
    }

    /* Title Styling */
    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 52px;
        color: #ffffff;
        margin: 0;
        line-height: 1.2;
    }

    /* Subtitle Styling */
    .sub-title {
        font-size: 22px;
        color: #8b949e;
        margin-top: 10px;
        margin-bottom: 40px;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        max-width: 500px;
        border-radius: 12px;
        background: linear-gradient(90deg, #FF4B4B, #FF1F1F);
        color: white !important;
        height: 3.5em;
        font-weight: bold;
        font-size: 18px;
        border: none;
        margin: 0 auto;
        display: block;
    }
    
    /* Center File Uploader */
    .uploadedFile { text-align: center; }
    .stFileUploader label { display: flex; justify-content: center; font-size: 18px !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# 2. Hero Section: Image + Title + Subtitle (Absolute Center)
# -------------------------------------------------------------------
try:
    # Trying to find your photo in GitHub
    img_path = "my_photo.jpg.jpeg"
    if not os.path.exists(img_path):
        img_path = "logo.jpeg"
        
    img_base64 = get_image_base64(img_path)
    
    # Injecting Image and Text inside a centered DIV
    st.markdown(f"""
        <div class="hero-section">
            <img src="data:image/jpeg;base64,{img_base64}" class="profile-pic">
            <h1 class="main-title">Solaiman Transcript & SEO</h1>
            <p class="sub-title">Your AI-Powered Video Content & SEO Automation Tool</p>
        </div>
        """, unsafe_allow_html=True)
except:
    # Fallback if image loading fails
    st.markdown("""
        <div class="hero-section">
            <h1 class="main-title">Solaiman Transcript & SEO</h1>
            <p class="sub-title">Your AI-Powered Video Content & SEO Automation Tool</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# 3. Upload and Result Section (English)
# -------------------------------------------------------------------
# Centering the uploader area
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    uploaded_file = st.file_uploader("📂 Upload your video file here", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.video(uploaded_file)
        
        if st.button("Generate SEO Content ✨"):
            with st.spinner('AI is processing your video... Please wait!'):
                with open("temp_vid.mp4", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Transcription
                model = whisper.load_model("base")
                result = model.transcribe("temp_vid.mp4")
                text = result['text']
                
                st.success("✅ Success! SEO Content Generated.")
                st.divider()
                
                # English UI Results
                st.markdown("### 📌 1. Optimized Video Title")
                st.code(f"Viral Content: {text[:60]}... 🔥")
                
                st.markdown("### 📝 2. Full Video Transcript (Bengali)")
                st.text_area("Transcript:", value=text, height=250)
                
                st.markdown("### 📄 3. SEO Friendly Description")
                st.info(f"Hi Everyone! In this video, we talked about {text[:150]}. \n\n#SolaimanSEO #BengaliAI")
                
                st.markdown("### #️⃣ 4. Viral Hashtags")
                st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent")
                
                st.markdown("### 🔑 5. Keywords & Tags")
                st.code("Solaiman Transcript, Video SEO Tool, AI Content Creator")

st.markdown("<br><hr><center><p style='color:#555;'>Developed by Solaiman | Powered by AI Technology © 2026</p></center>", unsafe_allow_html=True)
