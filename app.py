import streamlit as st
from PIL import Image
import io
from colorizer import colorize

# Page config
st.set_page_config(page_title="Gray2Color", page_icon="🌈", layout="centered")

# Title
st.title("🌈 Gray2Color")
st.write("Upload a black & white photo and let AI bring it to life with colors.🎨")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Resize to save memory
    MAX_SIZE = (1024, 1024)
    image = Image.open(uploaded_file).convert("RGB")
    image.thumbnail(MAX_SIZE)
    
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Use form for the Colorize button only
    with st.form("colorize_form"):
        submit = st.form_submit_button("✨ Colorize")

    # Only run colorization if button clicked
    if submit:
        with st.spinner("Colorizing... ⏳"):
            result = colorize(image)
            st.image(result, caption="Colorized Image", use_container_width=True)

            # Move download button **outside the form**
            buf = io.BytesIO()
            result.save(buf, format="PNG")
            st.download_button(
                "⬇️ Download Colorized Image",
                data=buf.getvalue(),
                file_name="colorized.png",
                mime="image/png"
            )
