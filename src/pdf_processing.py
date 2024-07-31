from pdf2image import convert_from_path
import pytesseract as tsr

def extract_text_from_pdf(pdf_path):
    text = ""
    pages = convert_from_path(pdf_path)
    for page in pages:
        page_text = tsr.image_to_string(page)
        text += page_text
    return text
