import streamlit as st

st.title('参考にしたURLや動画')

st.subheader('動画貼り付けの例')
video_url = 'https://www.youtube.com/watch?v=4nsTce1Oce8&t=1149s'
st.video(video_url)

st.subheader('マークダウンでリンク貼り付けの例')
st.markdown("[Googleはこちら](https://google.com)", unsafe_allow_html=True)

st.subheader('リンクボタンでリンク貼り付けの例')
st.link_button("Streamlitアプリへのアクセスがモバイル端末からかどうか調べる", "https://qiita.com/ak-sakatoku/items/ebc9d983234ba08b2f00")