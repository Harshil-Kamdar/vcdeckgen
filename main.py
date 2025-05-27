from parser.document_loader import load_document
from generator.summarizer import summarize_content
from generator.chart_builder import generate_charts
from generator.image_generator import generate_images
from generator.slide_maker import build_presentation

def main(input_path):
    print("[*] Loading document...")
    text = load_document(input_path)

    print("[*] Summarizing content...")
    slides = summarize_content(text)

    print("[*] Generating visuals...")
    charts = generate_charts(slides)
    images = generate_images(slides)

    print("[*] Building presentation...")
    build_presentation(slides, charts, images)

if __name__ == "__main__":
    input_path = "sample_business_doc.docx"  # Example input path
    main(input_path)
