import cv2 as cv
import pytesseract as tsr

def extract_text_from_image(image_path):
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    text = tsr.image_to_string(gray)
    return text
