import torch
import streamlit as st
from diffusers import StableDiffusionPipeline

@st.cache(allow_output_mutation=True)
def load_model(model_name):
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
    return pipe

models = load_model("CompVis/stable-diffusion-v1-4")
models = models.to("cuda")


def generate_image(prompt):
    image = models(prompt).image[0]
    return image

