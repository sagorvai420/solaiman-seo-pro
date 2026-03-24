import streamlit as st
import whisper
import os
from PIL import Image

# 1. App Configuration
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# Custom Styling for Centering everything
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #FF4B4B, #FF1F1F); color: white; height: 3.5em; font-weight: bold; font-size: 18px; border: none; }
    .header-box { text-align: center; padding-top: 30px; }
    .main-title { font-size: 45px; font-weight: 800; color: #ffffff; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #8b949e; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Centered Layout (Photo then Title)
st.markdown('<div class="header-box">', unsafe_allow_html=True)

# Centering the Image
col_a, col_b, col_c = st.columns([1, 1, 1])
with col_b:
    try:
        # Using your exact photo name from GitHub
        img = Image.open("my_photo.jpg.jpeg")
        st.image(img, width=250)
    except:
        st.info("📸 Logo is loading...")

# Centered Title and Subtitle
st.markdown('<h1 class="main-title">Solaiman Transcript & SEO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your Pro AI Tool for Video Content Automation</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 3. Video Upload Section (English)
uploaded_file = st.file_uploader("📂 Upload your video file here", type=["mp4", "mov", "avi", "mpeg4"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("Generate Content ✨"):
        with st.spinner('AI is analyzing your video... Please wait!'):
            # Save temporary file
            with open("temp_video.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Transcription logic
            model = whisper.load_model("base")
            result = model.transcribe("temp_video.mp4")
            text = result['text']
            
            st.success("✅ Process Completed Successfully!")
            
            # --- Results ---
            st.markdown("### 📌 1. Optimized Video Title")
            st.code(f"Viral Content: {text[:60]}... 🔥")
            
            st.markdown("### 📝 2. Full Bengali Transcript")
            st.text_area("Your Video Transcript:", value=text, height=250)
            
            st.markdown("### 📄 3. SEO Friendly Description")
            st.info(f"Hi Everyone! In this video, we talked about {text[:150]}. Hope you find it useful. \n\n#SolaimanSEO #VideoAutomation #BengaliContent")
            
            st.markdown("### #️⃣ 4. Viral Hashtags")
            st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralVideo #YouTubeTips #SEO2026")
            
            st.markdown("### 🔑 5. Keywords & Tags")
            st.code("Solaiman Transcript, AI Transcription, Video SEO Tool, Bengali Content Creation")
            
            st.markdown("### 🖼️ 6. Thumbnail Suggestion")
            st.warning(f"Strategy: Place your photo on the left and write: '{text[:25]}' in bold fonts.")

# Footer
st.markdown("<br><hr><center><p style='color:#555;'>Developed by Solaiman | Powered by AI Technology © 2026</p></center>", unsafe_allow_html=True)
