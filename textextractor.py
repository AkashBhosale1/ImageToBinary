#Upload your cloud vision credential files 
#upload Image

#Convert image into text

pip install google-cloud-vision

import tensorflow as tf
import os,io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd
from google.oauth2 import service_account

#credentials of google api
credentials = service_account.Credentials.from_service_account_file('your_credential_file.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

# image path
IMAGE_FILE = 'image.jpg'
FILE_PATH = os.path.join( IMAGE_FILE)

#load image
with io.open(FILE_PATH ,'rb') as image_file:
  content = image_file.read()

#extract text using reponse
image = vision.Image(content =content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text
#print(docText)
with open('image_to_text.txt', 'w') as f:
    f.write(docText)