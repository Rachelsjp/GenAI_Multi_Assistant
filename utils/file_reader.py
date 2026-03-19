from pypdf import PdfReader
import docx

def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "".join([p.extract_text() or "" for p in reader.pages])

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    return None