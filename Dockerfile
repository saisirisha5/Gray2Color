FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set Streamlit config directory
ENV STREAMLIT_HOME=/app/.streamlit

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.headless=true"]
