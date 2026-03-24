import streamlit as st
import whisper
import os
from PIL import Image

# 1. App Configuration & Theme
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# Custom CSS for perfect centering of Photo, Title, and Subtitle
st.markdown("""
    <style>
    /* Background and Global Color */
    .main { background-color: #0e1117; color: white; }
    
    /* Centering the Header Container */
    .header-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding-top: 30px;
    }

    /* Professional Title Style */
    .main-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 50px;
        color: #ffffff;
        margin-top: 15px;
        margin-bottom: 0px;
    }

    /* Professional Sub-title Style */
    .sub-title {
        font-size: 20px;
        color: #8b949e;
        margin-bottom: 40px;
    }

    /* Red Action Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #FF4B4B, #FF1F1F);
        color: white;
        height: 3.5em;
        font-weight: bold;
        font-size: 19px;
        border: none;
        margin-top: 20px;
    }

    /* Center the file uploader */
    .stFileUploader label {
        display: flex;
        justify-content: center;
        color: #ffffff !important;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# ২. লোগো ও টাইটেল সেকশন (সবকিছু মাঝখানে রাখার জন্য)
# -------------------------------------------------------------------
st.markdown('<div class="header-box">', unsafe_allow_html=True)

# মাঝখানে ছবি আনার জন্য কলাম ব্যবহার
col_l, col_m, col_r = st.columns([1, 1, 1])
with col_m:
    try:
        # এখানে আপনার ছবির নাম দিন। গিটহাবে যে নাম আছে সেটি দিন।
        # উদাহরণস্বরূপ: logo.jpeg অথবা my_photo.jpg.jpeg
        img = Image.open("logo.jpeg") 
        st.image(img, width=280)
    except:
        try:
            img = Image.open("my_photo.jpg.jpeg")
            st.image(img, width=280)
        except:
            st.error("⚠️ Photo NOT found in GitHub! Please rename your photo to 'logo.jpeg'")

# টাইটেল ও সাব-টাইটেল (একদম মাঝখানে থাকবে)
st.markdown('<h1 class="main-title">Solaiman Transcript & SEO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your AI-Powered Video Content & SEO Automation Tool</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# ৩. ভিডিও আপলোড ও রেজাল্ট সেকশন (ইংরেজিতে)
# -------------------------------------------------------------------
# আপলোডার মাঝামাঝি করার জন্য কলাম ব্যবহার
u_l, u_m, u_r = st.columns([1, 3, 1])
with u_m:
    uploaded_file = st.file_uploader("📂 Upload your video file here", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.video(uploaded_file)
        
        if st.button("Start AI Processing ✨"):
            with st.spinner('AI is analyzing your video... Please wait, Solaiman!'):
                # ভিডিও সেভ
                with open("temp_vid.mp4", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # ট্রান্সক্রিপশন
                model = whisper.load_model("base")
                result = model.transcribe("temp_vid.mp4")
                text = result['text']
                
                st.success("✅ Success! Your content is ready below.")
                st.divider()
                
                # ৫. রেজাল্ট প্রদর্শন (সব ইংরেজিতে)
                st.markdown("### 📌 1. Optimized Video Title")
                st.code(f"Viral Video: {text[:60]}... 🔥")
                
                st.markdown("### 📝 2. Full Bengali Transcript")
                st.text_area("Video Text:", value=text, height=250)
                
                st.markdown("### 📄 3. SEO Friendly Description")
                st.info(f"Hi Everyone! In this video, we talked about {text[:150]} in detail. Don't forget to like and share! \n\n#SolaimanSEO #BengaliContent")
                
                st.markdown("### #️⃣ 4. Viral Hashtags")
                st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent #YouTubeSEO")
                
                st.markdown("### 🔑 5. Keywords & Tags")
                st.code("Solaiman Transcript, Video SEO Tool, Bengali AI Automation")
                
                st.markdown("### 🖼️ 6. Thumbnail Strategy")
                st.warning(f"Suggestion: Place your photo on the left and write: '{text[:25]}' in bold text.")

# Footer
st.markdown("<br><hr><center><p style='color:#555;'>Developed by Solaiman | Powered by AI Technology © 2026</p></center>", unsafe_allow_html=True)
