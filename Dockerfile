FROM python:3.10-slim

# Set working directory
WORKDIR /gray2Color

# Copy project files
COPY . /gray2Color

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create and fix permissions for Streamlit folder
RUN mkdir -p /gray2Color/.streamlit && chmod -R 777 /gray2Color/.streamlit

# Copy Streamlit config file
COPY .streamlit/config.toml /gray2Color/.streamlit/config.toml

# Environment variables for Streamlit
ENV STREAMLIT_HOME=/gray2Color/.streamlit
ENV STREAMLIT_CONFIG_DIR=/gray2Color/.streamlit
ENV HOME=/gray2Color

# Expose Streamlit port
EXPOSE 7860

# Start Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0", "--server.headless=true"]
