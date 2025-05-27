import streamlit as st
from parser.document_loader import load_document
from generator.summarizer import summarize_content
from generator.chart_builder import generate_charts
from generator.image_generator import generate_images
from generator.slide_maker import build_presentation
import os

st.set_page_config(page_title="VCDeckGen", layout="centered")
st.title("📊 VCDeckGen: AI Investor Pitch Deck Generator")

uploaded_file = st.file_uploader("Upload your business plan (.docx or .txt)", type=["docx", "txt"])
if uploaded_file:
    with open("uploaded_input.docx", "wb") as f:
        f.write(uploaded_file.read())
    st.success("File uploaded successfully!")

    if st.button("Generate Deck"):
        st.info("Generating deck, please wait...")

        text = load_document("uploaded_input.docx")
        slides = summarize_content(text)
        charts = generate_charts(slides)
        images = generate_images(slides)
        build_presentation(slides, charts, images)

        st.success("Pitch deck generated!")
        with open("output/final_presentation.pptx", "rb") as file:
            st.download_button("📥 Download Pitch Deck", file, "Pitch_Deck.pptx")
