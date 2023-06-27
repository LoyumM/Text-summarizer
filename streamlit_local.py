import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline

def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

st.title("Text summarizer")

para = st.text_area("Enter paragraph")
summary = st.button("Summarize")

if summary:
    st.subheader("Summary:")
    st.write(predict_route(para))
