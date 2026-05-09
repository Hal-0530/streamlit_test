import streamlit as st
from PIL import Image
import os
from pathlib import Path

# ユーザーエージェントに基づいてモバイル端末かどうかを判定する関数
# 判定に失敗した場合はif_failedの値を返す。デフォルトはFalse
def st_is_mobile(if_failed=False):
    if st.context:
        headers = st.context.headers
        user_agent_string = headers.get("User-Agent", "")
        if not user_agent_string:
            return if_failed
        ua = user_agent_string.lower()
        # 以下、典型的なパターンごとに判定していく
        if 'iphone' in ua:
            return True
        if 'android' in ua and 'mobile' in ua:
            return True
        if 'windows phone' in ua:
            return True
        if 'blackberry' in ua:
            return True
    else:
        return if_failed
    return False

st.title('テストアプリ')
st.caption('これはStreallit習熟用のテストアプリです')

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

if st_is_mobile():
    st.write('モバイル端末でアクセスしています')
else:
    st.write('PC端末でアクセスしています')

st.page_link(current_dir / "pages/page_1.py", label="ページ1へ移動")
st.page_link(current_dir / "pages/page_2.py", label="ページ2へ移動")
st.page_link(current_dir / "pages/page_3.py", label="ページ3へ移動")
st.page_link(current_dir / "pages/page_4.py", label="ページ4へ移動")