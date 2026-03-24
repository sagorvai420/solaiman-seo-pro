import streamlit as st
import whisper
import os
import moviepy.editor as mp
from PIL import Image

# অ্যাপের কনফিগারেশন
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# ডিজাইন কাস্টমাইজেশন
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; height: 3em; font-weight: bold; }
    .css-10trblm { border-radius: 10px; padding: 20px; background-color: #262730; }
    </style>
    """, unsafe_allow_html=True)

# লোগো এবং টাইটেল
col1, col2 = st.columns([1, 4])
with col1:
    try:
        img = Image.open("my_photo.jpg")
        st.image(img, width=120)
    except:
        st.write("📸 Solaiman")
with col2:
    st.title("Solaiman Transcript & SEO")
    st.write("ভিডিও থেকে ট্রান্সক্রিপ্ট ও এসইও মেটাডাটা তৈরির প্রফেশনাল প্ল্যাটফর্ম।")

# ভিডিও ড্রপ জোন
uploaded_file = st.file_uploader("আপনার ভিডিও ফাইলটি এখানে ড্রপ করুন", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    if st.button("কন্টেন্ট জেনারেট করুন 🚀"):
        with st.spinner('একটু ধৈর্য ধরুন, সোলাইমান ভাই! আপনার ভিডিও প্রসেস হচ্ছে...'):
            # টেম্পোরারি ফাইল সেভ
            with open("temp_vid.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # ট্রান্সক্রিপশন
            model = whisper.load_model("base")
            result = model.transcribe("temp_vid.mp4")
            text = result['text']
            
            # এসইও জেনারেশন (অটোমেটেড)
            st.divider()
            st.header("✨ রেজাল্ট তৈরি!")
            
            # ১. টাইটেল
            st.subheader("📌 টাইটেল (Title):")
            st.code(f"অসাধারণ ভিডিও: {text[:50]}... 🔥")
            
            # ২. ডেসক্রিপশন
            st.subheader("📄 এসইও ফ্রেন্ডলি ডেসক্রিপশন:")
            st.info(f"এই ভিডিওতে আমরা বিস্তারিত আলোচনা করেছি {text[:150]} নিয়ে। ভিডিওটি ভালো লাগলে আমাদের সাথেই থাকুন। \n\n#SolaimanSEO #VideoAutomation")
            
            # ৩. ট্রান্সক্রিপ্ট
            st.subheader("📝 বাংলা ট্রান্সক্রিপ্ট:")
            st.text_area("", text, height=200)
            
            # ৪. হ্যাশট্যাগ
            st.subheader("#️⃣ হ্যাশট্যাগ (Hashtags):")
            st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent #YouTubeTools")
            
            # ৫. কীওয়ার্ড
            st.subheader("🔑 কীওয়ার্ড ট্যাগ (Keywords):")
            st.code("সোলাইমান অ্যাপ, ভিডিও ট্রান্সক্রিপ্ট, বাংলা এসইও, ইউটিউব ভিডিও অপ্টিমাইজেশন")
            
            # ৬. থাম্বনেইল গাইড
            st.subheader("🖼️ থাম্বনেইল সাজেশান:")
            st.warning(f"থাম্বনেইলে আপনার দেওয়া ছবির পাশে লিখুন: '{text[:25]}' - এটি বেশি ক্লিক পেতে সাহায্য করবে।")

st.markdown("---")
st.caption("Solaiman Transcript & SEO © 2026 | পাওয়ারড বাই কৃত্রিম বুদ্ধিমত্তা")
