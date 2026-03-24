import streamlit as st
import whisper
import os
import moviepy.editor as mp
from PIL import Image

# ১. অ্যাপের প্রফেশনাল ডিজাইন ও সেটআপ
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# ডার্ক থিম স্টাইল
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; height: 3.5em; font-weight: bold; font-size: 18px; border: none; }
    .stButton>button:hover { background-color: #ff3333; color: white; }
    .css-10trblm { border-radius: 15px; padding: 25px; background-color: #1a1c24; border: 1px solid #30363d; }
    h1 { color: #ffffff; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

# ২. লোগো এবং টাইটেল সেকশন
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        img = Image.open("my_photo.jpg")
        st.image(img, width=180, use_column_width=False)
    except:
        st.info("আপনার ছবিটি 'my_photo.jpg' নামে আপলোড করুন")
    st.markdown("<h1>Solaiman Transcript & SEO</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; color: #8b949e;'>আপনার ভিডিওকে প্রফেশনাল এসইও কন্টেন্টে রূপান্তর করুন</p>", unsafe_allow_html=True)

st.divider()

# ৩. ভিডিও আপলোড এরিয়া
uploaded_file = st.file_uploader("আপনার ভিডিও ফাইলটি এখানে ড্রপ করুন (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("ম্যাজিক শুরু করুন ✨"):
        with st.spinner('একটু অপেক্ষা করুন, সোলাইমান ভাই! AI আপনার ভিডিও প্রসেস করছে...'):
            # ফাইল সেভ করা
            with open("temp_vid.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # অডিও বের করা ও ট্রান্সক্রিপ্ট করা
            model = whisper.load_model("base")
            result = model.transcribe("temp_vid.mp4")
            text = result['text']
            
            # রেজাল্ট প্রদর্শন
            st.success("অভিনন্দন! আপনার কন্টেন্ট তৈরি।")
            
            # ডিজাইন বক্সে রেজাল্ট দেখানো
            st.markdown("### 📌 ১. ভিডিও টাইটেল (Title)")
            st.code(f"অসাধারণ ভিডিও: {text[:60]}... 🔥")
            
            st.markdown("### 📝 ২. সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট")
            st.text_area("ভিডিওর সব কথা নিচে লেখা হলো:", text, height=250)
            
            st.markdown("### 📄 ৩. এসইও ফ্রেন্ডলি ডেসক্রিপশন")
            desc = f"নমস্কার বন্ধুরা, আজকের ভিডিওতে আমরা বিস্তারিত আলোচনা করেছি {text[:150]} নিয়ে। ভিডিওটি ভালো লাগলে লাইক দিন এবং শেয়ার করুন। \n\n#SolaimanSEO #VideoAutomation #BengaliContent"
            st.info(desc)
            
            st.markdown("### #️⃣ ৪. ভাইরাল হ্যাশট্যাগ (Hashtags)")
            st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent #YouTubeTips #SEO2026")
            
            st.markdown("### 🔑 ৫. কীওয়ার্ড ট্যাগ (Keywords)")
            st.code("সোলাইমান ট্রান্সক্রিপ্ট, ভিডিও এসইও টুল, বাংলা ভিডিও অটোমেশন, YouTube SEO, Transcript Generator")
            
            st.markdown("### 🖼️ ৬. থাম্বনেইল আইডিয়া")
            st.warning(f"টিপস: থাম্বনেইলের বাম পাশে আপনার ছবি দিন এবং ডান পাশে বড় করে লিখুন: '{text[:25]}'")

st.markdown("<br><hr><center>Developed by Solaiman | Powered by AI Technology</center>", unsafe_allow_html=True)
