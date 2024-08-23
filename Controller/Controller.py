import sys
import os
import tempfile

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(__file__)


from Model.transcribe_text import transcribe
from Model.logo_detector import detect_logo
from Model.gemini import classify_text

def process_image_file(uploaded_image):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_image.read())
        temp_file_path = temp_file.name

    try:
        transcribed_text = transcribe(temp_file_path)
        logos = detect_logo(temp_file_path)
        return classify_text(transcribed_text, logos, temp_file_path)
    finally:
        os.remove(temp_file_path)