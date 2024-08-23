import sys
import os
import streamlit as st
from PIL import Image
import io

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Controller.Controller import process_image_file




st.title('Phishing Detection System')


image_file = st.file_uploader("Upload your image file", type=['jpg', 'png', 'jpeg'])

if image_file is not None:
    with st.spinner('Processing...'):
        text = process_image_file(image_file)
        st.write("Output:")
        st.write(text)