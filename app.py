import streamlit as st
import whisper
import os
from PIL import Image

# ১. অ্যাপের প্রফেশনাল ডিজাইন ও পেজ সেটআপ
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# কাস্টম ডিজাইন (CSS) - সবকিছু মাঝখানে আনার জন্য
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 15px; background-color: #FF4B4B; color: white; height: 3.5em; font-weight: bold; border: none; font-size: 18px;}
    h1 { color: #ffffff; text-align: center; margin-top: -10px; font-size: 45px; }
    .centered-img { display: block; margin-left: auto; margin-right: auto; border-radius: 50%; border: 5px solid #FF4B4B; }
    p { text-align: center; color: #8b949e; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# ২. লোগো এবং টাইটেল সেকশন (মাঝামাঝি করার জন্য)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # আপনার গিটহাবের ছবির নাম অনুযায়ী এখানে সেট করা হয়েছে
        img = Image.open("my_photo.jpg.jpeg")
        st.image(img, width=250) 
    except:
        st.markdown("<h2 style='text-align: center;'>📸 লোগো পাওয়া যায়নি</h2>", unsafe_allow_html=True)
    
    # ছবির নিচে বড় করে নাম
    st.markdown("<h1>Solaiman Transcript & SEO</h1>", unsafe_allow_html=True)
    st.markdown("<p>আপনার ভিডিওর ট্রান্সক্রিপ্ট ও এসইও অটোমেশন টুল</p>", unsafe_allow_html=True)

st.divider()

# ৩. ভিডিও আপলোড সেকশন
uploaded_file = st.file_uploader("আপনার ভিডিও ফাইলটি এখানে ড্রপ করুন (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    
    if st.button("ম্যাজিক শুরু করুন ✨"):
        with st.spinner('একটু অপেক্ষা করুন, সোলাইমান ভাই! AI আপনার ভিডিও প্রসেস করছে...'):
            # ভিডিও সেভ করা
            with open("temp_vid.mp4", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # ৪. ভিডিও থেকে ট্রান্সক্রিপ্ট করা
            model = whisper.load_model("base")
            result = model.transcribe("temp_vid.mp4")
            text = result['text']
            
            # ৫. রেজাল্ট প্রদর্শন
            st.success("অভিনন্দন! আপনার কন্টেন্ট এখন ব্যবহারের জন্য তৈরি।")
            
            st.markdown("### 📌 ১. আকর্ষণীয় টাইটেল (Title)")
            st.code(f"অসাধারণ ভিডিও: {text[:60]}... 🔥")
            
            st.markdown("### 📝 ২. সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট")
            st.text_area("ভিডিওর সব কথা নিচে লেখা হলো:", text, height=250)
            
            st.markdown("### 📄 ৩. এসইও ফ্রেন্ডলি ডেসক্রিপশন")
            desc = f"নমস্কার বন্ধুরা, আজকের ভিডিওতে আমরা বিস্তারিত আলোচনা করেছি {text[:150]} নিয়ে। ভিডিওটি ভালো লাগলে লাইক ও শেয়ার করুন। \n\n#SolaimanSEO #BengaliContent #VideoAutomation"
            st.info(desc)
            
            st.markdown("### #️⃣ ৪. ভাইরাল হ্যাশট্যাগ (Hashtags)")
            st.code("#SolaimanTranscript #BengaliAI #VideoSEO #ViralContent #YouTubeTips")
            
            st.markdown("### 🔑 ৫. কীওয়ার্ড ট্যাগ (Keywords)")
            st.code("সোলাইমান ট্রান্সক্রিপ্ট, ভিডিও এসইও টুল, বাংলা ভিডিও অটোমেশন, YouTube SEO, Transcript Generator")
            
            st.markdown("### 🖼️ ৬. থাম্বনেইল আইডিয়া")
            st.warning(f"থাম্বনেইল টিপস: মাঝখানে আপনার ছবি দিন এবং পাশে বড় করে লিখুন: '{text[:25]}'")

st.markdown("<br><hr><center>Developed by Solaiman | Powered by AI Technology</center>", unsafe_allow_html=True)
