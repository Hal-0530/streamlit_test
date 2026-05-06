import streamlit as st
from PIL import Image
import os

st.title('メインアプリ')
st.caption('これはメインアプリです')

image_path = './data/logo.png'

if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption=f'ロゴ画像:{image_path}', width=200)
else:
    # どこを探して失敗したか画面に表示させる（デバッグ用）
    st.error(f"ファイルが見つかりません。検索パス: {image_path}")
    # 念のため、カレントディレクトリの中身を表示して確認
    st.write(f"現在の作業ディレクトリ: {os.getcwd()}")