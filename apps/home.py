import streamlit as st
from PIL import Image

def app():
    st.balloons()
    st.subheader("""
    This server is used to predict 1-methyladenosine sites.This server is used to predict 1-methyladenosine sites.This server is used to predict 1-methyladenosine sites.""")
    image = Image.open('m1A_image.png')
    st.image(image)
    st.subheader("""
    The server m1A-Pred is built on Extreme Gradient Boos model. The server m1A-Pred is built on Extreme Gradient Boos model""")


