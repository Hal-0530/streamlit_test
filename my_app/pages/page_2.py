import streamlit as st
import datetime

# 左右に設置した箱（コンテナ）の高さを数値（pixel）で指定する
container_height = 300

st.title('フォームと画面分割の例')

col1, col2 = st.columns(2)
with col1:

    # st.formからst.containerに変更。ボタンに反応して処理を行う部分を別のフォームに移動したところエラーが出たため、フォームは使わない
    with st.container(border=True, height=container_height):
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

        #ボタン form_submit_buttonはフォーム内でしか使えないため、通常のbuttonに変更
        submit_btn = st.button('送信')
        cancel_btn = st.button('キャンセル')

with col2:
    # st.formからst.containerに変更。ボタンに反応して処理を行う部分を別のフォームに移動したところエラーが出たため、フォームは使わない
    with st.container(border=True, height=container_height):
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