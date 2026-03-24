import streamlit as st
import whisper
import os
import moviepy.editor as mp
from PIL import Image

st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; height: 3.5em; font-weight: bold; border: none; }
    h1 { color: #ffffff; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # এখানে আপনার ছবির নতুন নাম দেওয়া হয়েছে
        img = Image.open("my_photo.jpg.jpeg")
        st.image(img, width=180)
    except:
        st.info("লোগো লোড হচ্ছে...")
    st.markdown("<h1>Solaiman Transcript & SEO</h1>", unsafe_allow_html=True)

st.divider()
uploaded_file = st.file_uploader("আপনার ভিডিও ফাইলটি এখানে ড্রপ করুন", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    if st.button("ম্যাজিক শুরু করুন ✨"):
        with st.spinner('একটু অপেক্ষা করুন, সোলাইমান ভাই! AI আপনার ভিডিও প্রসেস করছে...'):
            with open("temp_vid.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            model = whisper.load_model("base")
            result = model.transcribe("temp_vid.mp4")
            text = result['text']
            
            st.success("অভিনন্দন! আপনার কন্টেন্ট তৈরি।")
            st.subheader("📌 ১. ভিডিও টাইটেল (Title)")
            st.code(f"অসাধারণ ভিডিও: {text[:60]}... 🔥")
            st.subheader("📝 ২. সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট")
            st.text_area("", text, height=250)
            st.subheader("📄 ৩. এসইও ফ্রেন্ডলি ডেসক্রিপশন")
            st.info(f"এই ভিডিওতে আমরা বিস্তারিত আলোচনা করেছি {text[:150]} নিয়ে। #SolaimanSEO")
            st.subheader("#️⃣ ৪. ভাইরাল হ্যাশট্যাগ")
            st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent")
            st.subheader("🔑 ৫. কীওয়ার্ড ট্যাগ")
            st.code("সোলাইমান ট্রান্সক্রিপ্ট, ভিডিও এসইও টুল, ইউটিউব এসইও")

st.markdown("<br><hr><center>Developed by Solaiman</center>", unsafe_allow_html=True)
