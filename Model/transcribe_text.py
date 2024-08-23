import pytesseract
from PIL import Image, ImageEnhance

def enhance_image(image):
    return ImageEnhance.Contrast(image).enhance(2.0)

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def transcribe(uploaded_image):

    if uploaded_image is not None:
        image = enhance_image(Image.open(uploaded_image))
        return extract_text_from_image(image)

