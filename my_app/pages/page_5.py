import streamlit as st

st.title('データカウント')

st.subheader('このコードはうまくいかない例')

with st.container():
    code = '''
    st.write('ボタンを押してください')
    count = 0
    
    if st.button('push me', key='btn1'):
        st.write('ボタンを押しました')
        count += 1
    
    st.write('count = ', count)
    '''
    st.code(code, language='python')

    st.write('ボタンを押してください')
    count = 0
    
    if st.button('push me', key='btn1'):
        st.write('ボタンを押しました')
        count += 1
    
    st.write('count = ', count)

st.subheader('以下のコードはうまくいく例')

with st.container():
    code = '''
    if 'count' not in st.session_state:
        st.write('ボタンを押してください')
        st.session_state['count'] = 0
    
    if st.button('push me', key='btn2'):
        st.write('ボタンを押しました')
        st.session_state['count'] += 1
    
    st.write('count = ', st.session_state['count'])
    '''
    st.code(code, language='python')

    if 'count' not in st.session_state:
        st.write('ボタンを押してください')
        st.session_state['count'] = 0
    
    if st.button('push me', key='btn2'):
        st.write('ボタンを押しました')
        st.session_state['count'] += 1
    
    st.write('count = ', st.session_state['count'])