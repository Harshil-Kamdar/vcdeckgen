from docx import Document

def load_document(path):
    if path.endswith(".docx"):
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format. Use .docx or .txt.")
