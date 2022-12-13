# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:15:37 2022

@author: 91986
"""

import openai
import urllib.request
import streamlit as st
from PIL import Image

openai.api_key = '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'

def generate_image(image_description):
  image_as_response = openai.Image.create(
      
      prompt = image_description,
      n=1,
      size="512x512"
        )
    
  image_url = image_as_response['data'][0]['url']
  urllib.request.urlretrieve(image_url, 'picture.png')
  image = Image.open('picture.png')
  return image

st.title('Image Generator - OpenAI')
img_description = st.text_input('Type Out Image Description')

if st.button('Click to Generate Image'):
    generate_img = generate_image(img_description)
    st.image(generate_img)
    

