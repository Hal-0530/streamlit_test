import streamlit as st
from PIL import Image
import os
from pathlib import Path

st.title('メインアプリ')
st.caption('これはメインアプリです')

# main_app.pyから見て data/logo.png を読み込む場合
current_dir = Path(__file__).parent  # main_app.pyがあるフォルダ
file_path = current_dir / "data" / "logo.png"

if os.path.exists(file_path):
    image = Image.open(file_path)
    st.image(image, caption=f'ロゴ画像:{file_path}', width=200)
else:
    # どこを探して失敗したか画面に表示させる（デバッグ用）
    st.error(f"ファイルが見つかりません。検索パス: {file_path}")
    # 念のため、カレントディレクトリの中身を表示して確認
    st.write(f"現在の作業ディレクトリ: {os.getcwd()}")