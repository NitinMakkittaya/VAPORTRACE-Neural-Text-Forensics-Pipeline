import fitz  # PyMuPDF

def extract_text_from_pdf(file_stream):
    """Ingests a PDF byte stream and extracts structural text."""
    doc = fitz.open(stream=file_stream, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def parse_input(request):
    """Determines if input is raw text or a PDF file."""
    if 'pdf' in request.files:
        return extract_text_from_pdf(request.files['pdf'].read())
    return request.form.get('text', '')