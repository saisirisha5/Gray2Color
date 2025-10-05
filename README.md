<!-- ---
title: 🌈Gray2Color
sdk: docker
emoji: ⚡
colorFrom: indigo
colorTo: purple
app_file: app.py
pinned: false
--- -->

🎨 **See AI bring black & white photos to life!**  
[Try Gray2Color live →](https://saisirisha5-gray2color.hf.space/)

# 🌈 Gray2Color – Black & White Image Colorization

Gray2Color is an AI-powered tool that colorizes black and white images, bringing them to life with realistic colors using a pre-trained neural network. Users can upload any grayscale image, see the colorized result instantly, and download it. The app is built with **Streamlit** and deployed via **Docker** for Hugging Face Spaces.

---

## 🧠 Features

- Upload black & white images (jpg, jpeg, png)  
- AI-based colorization using a pre-trained model  
- Instant preview of colorized image  
- Download the colorized image  
- Modern, responsive Streamlit UI

---

## ⚙️ Requirements

- Python 3.7+  
- Streamlit  
- Pillow  
- NumPy  
- OpenCV  
- Torch (if your `colorizer` uses it)

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/Gray2Color.git
cd Gray2Color

2. Run the app:

```bash
streamlit run app.py

3.Open http://localhost:8501 in your browser.

4.Upload a black & white image, click Colorize, and download the output.

## 🔍Results

## 🤝 Credits
Model and resources by Richard Zhang et al.
GitHub: [richzhang/colorization](http://github.com/richzhang/colorization)

## Developed by [Sai Sirisha Devi Prabhala](https://github.com/saisirisha5) 