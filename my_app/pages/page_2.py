import streamlit as st
import datetime

st.title('フォームと画面分割の例')

col1, col2 = st.columns(2)
with col1:

    with st.form(key='my_form1'):
        #テキストボックス
        name = st.text_input('名前を入力してください')
        address = st.text_input('住所を入力してください')

        #セレクトボックス
        age_category = st.selectbox('年齢を選択してください', ['10代', '20代', '30代', '40代', '50代以上'])

        #ラジオボタン
        gender = st.radio('性別を選択してください', ['男性', '女性', 'その他'])

        #複数選択可能（マルチセレクト）
        hobbies = st.multiselect('趣味を選択してください', ['スポーツ', '音楽', '映画', '読書', '旅行', '料理', 'ゲーム', 'プログラミング', '釣り'])

        #スライダー
        height = st.slider('身長を選択してください', 50, 250, 170)
        weight = st.slider('体重を選択してください', 20, 200, 60)

        #日付
        start_date = st.date_input('開始日を選択してください', datetime.date.today())

        #カラーピッカー
        color = st.color_picker('好きな色を選択してください', '#00f900')

        #チェックボックス
        agree = st.checkbox('テストチェックボックスです')

        #ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

with col2:
    with st.form(key='my_form2'):
        if submit_btn:
            st.text(f'こんにちは、{name}さん！ 住所は{address}ですね！')
            st.text(f'年齢は{age_category}、性別は{gender}ですね！')
            st.text(f'身長は{height}cm、体重は{weight}kgですね！')
            st.text(f'趣味は{", ".join(hobbies)}ですね！')
            st.text(f'開始日は{start_date}ですね！')
            st.text(f'チェックボックスの状態: {agree}')
            st.write(f'好きな色は<span style="color:{color}">{color}</span>ですね！', unsafe_allow_html=True)

        if cancel_btn:
            st.text('キャンセルされました')