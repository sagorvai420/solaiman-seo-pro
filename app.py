import streamlit as st
import whisper
import os
from PIL import Image

# 1. App Configuration
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# Custom Styling for Perfect Centering & Dark Theme
st.markdown("""
    <style>
    /* Background and Global Styles */
    .main { background-color: #0e1117; color: white; }
    
    /* Centering Header Elements */
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding-top: 30px;
    }

    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 45px;
        color: #ffffff;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        color: #8b949e;
        margin-bottom: 40px;
    }

    /* Red Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #FF4B4B, #FF1F1F);
        color: white;
        height: 3.5em;
        font-weight: bold;
        font-size: 18px;
        border: none;
        margin-top: 10px;
    }
    
    /* Centering the File Uploader Label */
    .stFileUploader label {
        display: flex;
        justify-content: center;
        font-size: 18px !important;
        color: #ffffff !important;
    }

    /* Centering footer */
    .footer {
        text-align: center;
        padding: 50px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Centered Header Section (Photo then Title)
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# Centering Image using Columns
col_l, col_m, col_r = st.columns([1, 1, 1])
with col_m:
    try:
        # Checking for the photo in your GitHub
        img = Image.open("logo.jpeg")
        st.image(img, width=220)
    except:
        try:
            img = Image.open("my_photo.jpg.jpeg")
            st.image(img, width=220)
        except:
            st.warning("📸 Logo is loading... Please ensure image is uploaded in GitHub.")

# Title and Subtitle in English
st.markdown('<h1 class="main-title">Solaiman Transcript & SEO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your AI-Powered Video Content & SEO Automation Tool</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 3. Upload Section (English Interface)
# Centering uploader
u_col1, u_col2, u_col3 = st.columns([1, 3, 1])
with u_col2:
    uploaded_file = st.file_uploader("📂 Upload or Drag your video file here (MP4, MOV)", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.video(uploaded_file)
        
        # Processing Button
        if st.button("Start AI Magic ✨"):
            with st.spinner('Analyzing your video... Please wait, Solaiman!'):
                # Temporary file save
                with open("temp_vid.mp4", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Transcription Logic
                model = whisper.load_model("base")
                result = model.transcribe("temp_vid.mp4")
                text = result['text']
                
                st.success("✅ Success! Your SEO Content is ready below.")
                
                # 4. Results Section (English Labels)
                st.divider()
                st.markdown("### 📌 1. Optimized Video Title")
                st.code(f"Viral Video: {text[:60]}... 🔥")
                
                st.markdown("### 📝 2. Full Bengali Transcript")
                st.text_area("Video Text Output:", value=text, height=250)
                
                st.markdown("### 📄 3. SEO Friendly Description")
                desc = f"Hello everyone! In this video, we discussed {text[:150]} in detail. Don't forget to like and share! \n\n#SolaimanSEO #VideoAutomation #BengaliContent"
                st.info(desc)
                
                st.markdown("### #️⃣ 4. Viral Hashtags")
                st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent #YouTubeSEO")
                
                st.markdown("### 🔑 5. Keywords & Tags")
                st.code("Solaiman Transcript, Video SEO Tool, Bengali AI, YouTube Keywords")
                
                st.markdown("### 🖼️ 6. Thumbnail Design Idea")
                st.warning(f"Suggestion: Place your photo on the left and write: '{text[:25]}' in bold text on the right.")

# Footer Section
st.markdown('<div class="footer"><hr>Developed by Solaiman | Powered by AI Technology © 2026</div>', unsafe_allow_html=True)
