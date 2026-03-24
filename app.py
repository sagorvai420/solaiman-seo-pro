import streamlit as st
import moviepy.editor as mp
import whisper
import os
from PIL import Image

# ১. অ্যাপের কনফিগারেশন এবং লোগো সেটআপ
st.set_page_config(page_title="Solaiman Transcript & SEO", page_icon="🎯", layout="wide")

# কাস্টম সিএসএস স্টাইল (প্রফেশনাল লুকের জন্য)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    h1 {
        color: #1E1E1E;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ২. লোগো এবং টাইটেল
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # এখানে আপনার দেওয়া ছবিটি 'logo.jpg' নামে সেভ করে একই ফোল্ডারে রাখতে হবে
    try:
        img = Image.open("logo.jpg")
        st.image(img, width=150)
    except:
        st.info("আপনার ছবিটি 'logo.jpg' নামে অ্যাপ ফোল্ডারে রাখুন।")
    st.title("Solaiman Transcript & SEO")
    st.subheader("ভিডিও থেকে ট্রান্সক্রিপ্ট ও এসইও কন্টেন্ট জেনারেটর")

# ৩. ভিডিও আপলোড সেকশন
uploaded_file = st.file_uploader("আপনার ভিডিও ফাইলটি এখানে ড্রপ করুন (MP4, MOV, AVI)", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # ফাইল সেভ করা
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.video(uploaded_file)
    
    if st.button("প্রসেসিং শুরু করুন"):
        with st.spinner('অপেক্ষা করুন... ভিডিও থেকে অডিও আলাদা করা হচ্ছে এবং ট্রান্সক্রিপ্ট তৈরি হচ্ছে...'):
            
            # অডিও এক্সট্রাক্ট করা
            video = mp.VideoFileClip("temp_video.mp4")
            video.audio.write_audiofile("temp_audio.mp3")
            
            # ৪. ট্রান্সক্রিপ্ট তৈরি (Whisper AI ব্যবহার করে)
            # এটি স্বয়ংক্রিয়ভাবে বাংলা ভাষা শনাক্ত করবে
            model = whisper.load_model("base")
            result = model.transcribe("temp_audio.mp3")
            transcript_text = result['text']
            
            st.success("ট্রান্সক্রিপশন সম্পন্ন হয়েছে!")
            
            # ৫. এসইও কন্টেন্ট জেনারেশন (ডেমো হিসেবে টেক্সট প্রসেসিং)
            # এখানে আপনি OpenAI API কানেক্ট করলে আরও নিখুঁত রেজাল্ট পাবেন
            title = f"ভিডিওর টাইটেল: {transcript_text[:50]}..."
            description = f"এই ভিডিওতে আলোচনা করা হয়েছে: {transcript_text[:200]}। আশা করি ভিডিওটি আপনাদের উপকারে আসবে।"
            hashtags = "#SolaimanSEO #BengaliContent #ViralVideo #YouTubeTips"
            keywords = "বাংলা ভিডিও, টিউটোরিয়াল, Solaiman Transcript, SEO Tools"
            
            # ৬. আউটপুট প্রদর্শন
            st.divider()
            st.header("✨ আপনার ভিডিওর এসইও রেজাল্ট")
            
            # টাইটেল
            st.subheader("📌 টাইটেল (Title):")
            st.code(title)
            
            # ট্রান্সক্রিপ্ট
            st.subheader("📝 সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট:")
            st.text_area("", value=transcript_text, height=300)
            
            # ডেসক্রিপশন
            st.subheader("📄 এসইও ফ্রেন্ডলি ডেসক্রিপশন:")
            st.info(description)
            
            # হ্যাশট্যাগ
            st.subheader("#️⃣ হ্যাশট্যাগ (Hashtags):")
            st.code(hashtags)
            
            # কীওয়ার্ড
            st.subheader("🔑 কীওয়ার্ড ট্যাগ (Keywords):")
            st.code(keywords)
            
            # ৭. থাম্বনেইল আইডিয়া (ডিজাইন গাইড)
            st.subheader("🖼️ থাম্বনেইল ডিজাইন আইডিয়া:")
            st.warning("আপনার থাম্বনেইলে বড় করে লিখুন: '" + title[:30] + "' এবং পাশে আপনার প্রফেশনাল ছবিটি ব্যবহার করুন।")
            
            # ফাইলগুলো ডিলিট করা
            os.remove("temp_video.mp4")
            os.remove("temp_audio.mp3")

st.markdown("---")
st.caption("Developed by Solaiman | Powered by AI Technology")
