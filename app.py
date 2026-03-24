import streamlit as st
import whisper
import os
import google.generativeai as genai
from PIL import Image

# অ্যাপের টাইটেল ও লোগো সেটআপ
st.set_page_config(page_title="Solaiman Transcript & SEO", layout="wide")

# কাস্টম ডিজাইন (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #e63946; color: white; border-radius: 10px; font-weight: bold; }
    .seo-box { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# লোগো এবং নাম প্রদর্শন
col1, col2 = st.columns([1, 5])
with col1:
    try:
        # আপনার ছবি এখানে লোগো হিসেবে থাকবে
        img = Image.open("my_photo.jpg")
        st.image(img, width=120)
    except:
        st.write("📸 লোগো")

with col2:
    st.title("Solaiman Transcript & SEO")
    st.write("আপনার ভিডিওকে প্রফেশনাল এসইও কন্টেন্টে রূপান্তর করুন")

# ভিডিও আপলোড সেকশন
video_file = st.file_uploader("আপনার ভিডিও ড্রপ করুন", type=["mp4", "mov", "avi"])

if video_file:
    st.video(video_file)
    
    if st.button("ম্যাজিক শুরু করুন ✨"):
        with st.spinner('একটু অপেক্ষা করুন, সোলাইমান ভাই! আপনার ভিডিওর ট্রান্সক্রিপ্ট ও এসইও তৈরি হচ্ছে...'):
            
            # ভিডিও সেভ করা
            with open("temp_video.mp4", "wb") as f:
                f.write(video_file.getbuffer())

            # ১. ভিডিও থেকে বাংলা ট্রান্সক্রিপ্ট (Whisper AI)
            model = whisper.load_model("base")
            result = model.transcribe("temp_video.mp4")
            transcript_text = result['text']

            # ২. এসইও জেনারেটর (স্মার্ট প্রম্পট)
            # আপনি এখানে নিজের Gemini API Key বসালে রেজাল্ট আরও ভালো হবে
            title = f"ভিডিও টাইটেল: {transcript_text[:60]}... 🔥"
            description = f"বিস্তারিত ডেসক্রিপশন:\nনমস্কার বন্ধুরা, আজকের ভিডিওতে আমরা কথা বলেছি {transcript_text[:150]} নিয়ে। ভিডিওটি ভালো লাগলে শেয়ার করুন!"
            hashtags = "#SolaimanSEO #BengaliContent #ViralVideo2024 #YouTubeTips"
            keywords = "সোলাইমান ট্রান্সক্রিপ্ট, বাংলা এসইও টুল, ভিডিও কন্টেন্ট, মোটিভেশন"
            
            # ৩. রেজাল্ট প্রদর্শন
            st.success("কাজ শেষ! নিচে আপনার রেজাল্ট দেখুন:")
            
            st.markdown("### 📌 ১. ভিডিও টাইটেল")
            st.code(title)
            
            st.markdown("### 📝 ২. সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট")
            st.text_area("", transcript_text, height=250)
            
            st.markdown("### 📄 ৩. এসইও ফ্রেন্ডলি ডেসক্রিপশন")
            st.info(description)
            
            st.markdown("### #️⃣ ৪. ভাইরাল হ্যাশট্যাগ")
            st.code(hashtags)
            
            st.markdown("### 🔑 ৫. কীওয়ার্ড ট্যাগ")
            st.code(keywords)
            
            st.markdown("### 🖼️ ৬. থাম্বনেইল ডিজাইন আইডিয়া")
            st.warning(f"থাম্বনেইলে বড় করে লিখুন: '{transcript_text[:30]}' এবং আপনার হাসিমুখের ছবিটি বাম পাশে ব্যবহার করুন।")

st.markdown("---")
st.write("© ২০২৪ Solaiman Transcript & SEO | Developed for Excellence")
