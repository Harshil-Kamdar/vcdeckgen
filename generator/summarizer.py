def summarize_content(text):
    # Dummy segmentation for demo
    sections = [
        "Problem", "Solution", "Market Size", "Product/Tech",
        "Business Model", "Traction", "Team", "Financials", "Ask & Use of Funds"
    ]
    lines = text.split("\n")
    per_section = max(1, len(lines) // len(sections))
    slides = []
    for i, section in enumerate(sections):
        content = lines[i*per_section:(i+1)*per_section]
        slides.append({"title": section, "content": "\n".join(content)})
    return slides
