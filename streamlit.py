import gdown
import py7zr
import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

model_url = "https://drive.google.com/uc?export=download&id=15eD9fj2bJwH5Vg7mt1uXCdkO_Eb0OgiH"
file_path = "artifacts\model_trainer\pegasus-samsum-model-new.7z"
output_dir = "artifacts\model_trainer"

def download_file(url, output_path):
    gdown.download(url, output_path, quiet=False)

@st.cache_data     
def load_files(url, filename):
    download_file(url, filename)
    
def unzip_7zip(file_path, output_dir):
    with py7zr.SevenZipFile(file_path, mode='r') as archive:
        archive.extractall(path=output_dir)

def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

st.title("Text summarizer")

load_files(model_url, "artifacts\model_trainer\pegasus-samsum-model-new.7z")
unzip_7zip(file_path, output_dir)

para = st.text_area("Enter paragraph")
summary = st.button("Summarize")

if summary:
    st.subheader("Summary:")
    st.write(predict_route(para))
