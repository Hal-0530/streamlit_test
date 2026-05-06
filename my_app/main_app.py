import streamlit as st
from PIL import Image

st.title('メインアプリ')
st.caption('これはメインアプリです')

image = Image.open('./data/logo.png')
st.image(image, caption='ロゴ画像', width=200)