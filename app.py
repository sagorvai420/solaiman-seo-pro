import streamlit as st
import whisper
import os
import base64
from PIL import Image, ImageDraw, ImageFont
import io
import textwrap

# 1. App Configuration - English Name: Solaiman
st.set_page_config(page_title="Solaiman Transcript & SEO Pro", page_icon="🎨", layout="wide")

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- Custom Styling for Absolute Centering & English UI ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .header-section { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; width: 100%; padding-top: 30px; }
    .profile-pic { width: 230px; height: 230px; border-radius: 20px; border: 4px solid #FF4B4B; object-fit: cover; margin-bottom: 15px; box-shadow: 0px 0px 20px rgba(255, 75, 75, 0.4); }
    .main-title { font-family: 'Segoe UI', sans-serif; font-weight: 800; font-size: 50px; color: #ffffff; margin:0; }
    .sub-title { font-size: 18px; color: #8b949e; margin-bottom: 30px; }
    .stButton>button { width: 100%; max-width: 500px; border-radius: 12px; background: linear-gradient(90deg, #FF4B4B, #FF1F1F); color: white !important; height: 3.5em; font-weight: bold; font-size: 19px; border: none; display: block; margin: 0 auto; }
    .stFileUploader label { display: flex; justify-content: center; font-size: 18px !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Header Section - English Name: Solaiman
try:
    img_path = "logo.jpeg" if os.path.exists("logo.jpeg") else "my_photo.jpg.jpeg"
    img_base64 = get_image_base64(img_path)
    st.markdown(f'<div class="header-section"><img src="data:image/jpeg;base64,{img_base64}" class="profile-pic"><h1 class="main-title">Solaiman Transcript & SEO</h1><p class="sub-title">Your AI-Powered Video Content & SEO Automation Tool</p></div>', unsafe_allow_html=True)
except:
    st.markdown('<div class="header-section"><h1 class="main-title">Solaiman Transcript & SEO</h1></div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# 3. Professional Thumbnail Designer (Bengali Text)
# -------------------------------------------------------------------
def create_bangla_thumbnail(text, photo_path):
    width, height = 1280, 720
    img = Image.new('RGB', (width, height), color=(14, 17, 23))
    draw = ImageDraw.Draw(img)
    
    # Red Side Accent
    draw.rectangle([0, 0, 15, height], fill="#FF4B4B")
    
    # Paste User Photo on Left
    try:
        user_photo = Image.open(photo_path).convert("RGBA")
        user_photo.thumbnail((600, 600))
        img.paste(user_photo, (60, 60), user_photo if "A" in user_photo.getbands() else None)
    except:
        pass

    # Draw Bengali Text on Right
    try:
        font = ImageFont.truetype("font.ttf", 85)
    except:
        font = ImageFont.load_default()

    # Get catchy Bengali words for thumbnail
    clean_text = text[:80]
    lines = textwrap.wrap(clean_text, width=15)
    
    y_text = 180
    for line in lines[:2]:
        draw.text((680, y_text), line, font=font, fill="#FFFFFF")
        y_text += 130
    
    draw.text((680, 520), "ভাইরাল ভিডিও 🔥", font=font, fill="#FF4B4B")
    return img

# -------------------------------------------------------------------
# 4. Processing Logic (Interface: English | Output: Bengali)
# -------------------------------------------------------------------
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    # Uploader - Solaiman requested large file support
    uploaded_file = st.file_uploader("📂 Upload or Drag your Video/Audio (Supports Large Files)", type=["mp4", "mov", "avi", "mp3"])

    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' is uploaded successfully!")
        
        if st.button("Generate Pro Results 🚀"):
            with st.spinner('AI is analyzing... generating results in Bengali!'):
                with open("temp_file", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                model = whisper.load_model("base")
                result = model.transcribe("temp_file")
                transcript = result['text']
                
                st.balloons()
                st.success("✅ Success! Your Results are Ready.")
                
                # --- THUMBNAIL DESIGN ---
                st.subheader("🖼️ Your Auto-Designed Thumbnail")
                thumb_img = create_bangla_thumbnail(transcript, img_path)
                st.image(thumb_img)
                
                buf = io.BytesIO()
                thumb_img.save(buf, format="PNG")
                st.download_button("Download Thumbnail 📥", buf.getvalue(), "solaiman_thumbnail.png", "image/png")
                
                st.divider()
                
                # --- BENGALI SEO CONTENT ---
                st.markdown("### 📌 ১. ভিডিওর আকর্ষণীয় টাইটেল (Title)")
                st.code(f"ভাইরাল ভিডিও: {transcript[:50]}... 🔥")
                
                st.markdown("### 📝 ২. সম্পূর্ণ বাংলা ট্রান্সক্রিপ্ট (Transcript)")
                st.text_area("Video Text Output:", value=transcript, height=250)
                
                st.markdown("### 📄 ৩. এসইও ডেসক্রিপশন (SEO Description)")
                # Bengali Name Correction: সোলায়মান
                desc = f"নমস্কার বন্ধুরা! আজকের ভিডিওতে আমরা বিস্তারিত আলোচনা করেছি {transcript[:150]} নিয়ে। ভিডিওটি আপনাদের কাজে লাগলে লাইক ও শেয়ার করার অনুরোধ রইল। \n\n#সোলায়মানএসইও #SolaimanSEO #BengaliAutomation #YouTubeTips"
                st.info(desc)
                
                st.markdown("### #️⃣ ৪. ভাইরাল হ্যাশট্যাগ (Hashtags)")
                st.code("#সোলায়মানট্রান্সক্রিপ্ট #SolaimanTranscript #BengaliAI #VideoSEO #ViralVideo2026")
                
                st.markdown("### 🔑 ৫. কীওয়ার্ড এবং ট্যাগ (Keywords & Tags)")
                st.code("সোলায়মান ট্রান্সক্রিপ্ট, Solaiman SEO Tool, ভিডিও এসইও টুল, বাংলা এআই অটোমেশন")
                
                if os.path.exists("temp_file"):
                    os.remove("temp_file")

# Footer - Bengali Name: সোলায়মান
st.markdown("<br><hr><center><p style='color:#555;'>Developed by সোলায়মান | Powered by AI Technology © 2026</p></center>", unsafe_allow_html=True)
