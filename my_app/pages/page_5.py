import streamlit as st

st.title('データカウント')
 
st.write('変数を設定')
count = 0
 
if st.button('push me'):
    st.write('ボタンを押しました')
    count += 1
 
st.write('count = ', count)