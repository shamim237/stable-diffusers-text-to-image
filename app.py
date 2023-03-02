import streamlit as st
from model import generate_image

st.title("Text-to-Image Generation!")
prompt = st.text_input("Enter some to text to generate image....")


def process():
    image = generate_image(prompt)
    st.success(image)
st.button('Generate', on_click=process)