import streamlit as st

st.title('参考にしたURLや動画')

video_url = 'https://www.youtube.com/watch?v=4nsTce1Oce8&t=1149s'
st.video(video_url)

st.link_button("Streamlitアプリへのアクセスがモバイル端末からかどうか調べる", "https://qiita.com/ak-sakatoku/items/ebc9d983234ba08b2f00")