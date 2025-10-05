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
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("✨ Colorize"):
        with st.spinner("Colorizing... ⏳"):
            result = colorize(image)
            st.image(result, caption="Colorized Image", use_container_width=True)

            # Download button
            buf = io.BytesIO()
            result.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button("⬇️ Download Colorized Image", data=byte_im, file_name="colorized.png", mime="image/png")
