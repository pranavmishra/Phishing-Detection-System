import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure your API key
genai.configure(api_key=GOOGLE_API_KEY)

def classify_text(text, logos, uploaded_image):
    system_instructions = """
Given an image of a website and its transcribed text, extract and classify the following information:

Input:

Image: A visual representation of the website.
Text: The transcribed text from the image.
Output:

Known Context: A brief description of the website's purpose or topic.
Brand/Mark: Logos or brand names found on the website.
Keywords: A list of significant keywords extracted from the content.
Detected Objects: A description of any unusual or suspicious elements, such as forms, buttons, or links.
Summary: A concise overview of the website's content and purpose.
Classification: Legitimate, Phishing, Suspicious, or Unknown.
Explanation: A detailed explanation of the reasoning behind the classification.
Focus on Prices:

Pay close attention to prices of items. If a product is priced significantly higher or lower than expected, it could be a sign of a scam or phishing attempt.
Examples:

Image: Bank of America login page

Known Context: Bank login page
Brand/Mark: Bank of America
Keywords: Sign in, CreditCard, Online ID, Passcode, Transfer Funds, Online Banking
Detected Objects: Sign in form, Sign in button
Image: DPD delivery email

Known Context: Delivery notification email
Brand/Mark: DPD, Warning icon
Keywords: Delivery, package, parcel, unpaid customs duty, shipping fee
Detected Objects: Schedule new delivery button
Remember:

Analyze the visual elements of the website, such as the layout, color scheme, and overall design.
Consider the context of the information presented, such as the sender's email address or the domain name of the website.
Use your knowledge of common phishing tactics and scam techniques to identify suspicious elements.
    """

    template = f"""
    Known context = 

    Brand/Mark = {logos}

    Keywords = 

    Custom Detected Objects = 

    Summary

    Classification

    Explanation
"""
    model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=[system_instructions],
                                  generation_config={'temperature': 0})
    response = model.generate_content(['Template: ' + template,'Text: '+text, Image.open(uploaded_image)])
    model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="Your job is to rewrite any input you get in a better formatted way so that it looks more aesthetically pleasing. The output will be displayed on a streamlit app. It was be displayed using the streamlit.write() method.", generation_config={'temperature': 0})
    response = model.generate_content([response.text])
    classification = response.text


    return classification


