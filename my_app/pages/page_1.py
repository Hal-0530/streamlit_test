import streamlit as st

st.title('コード内容')

st.subheader('メインページ')

code = '''
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
'''
st.code(code, language='python')


st.subheader('Page_2')
code = '''
import streamlit as st
import datetime

st.subheader('フォームの例')

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
'''
st.code(code, language='python')

st.subheader('Page_3')
code = '''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
from pathlib import Path

#データ分析関連
st.subheader('データ分析関連')

# 辻堂気象データ.csv のパスを指定する
dir = Path(__file__).parents[1]  # page_3.pyの親の親フォルダ
file_path = dir / "data" / "辻堂気象データ.csv"
# フォントのパスを指定する（matplotlibで日本語を表示するため）
dir = Path(__file__).parents[2]  # page_3.pyの親の親フォルダ
font_path = dir / "fonts" / "ipaexg.ttf"
# フォントファイルが存在するか確認してから設定する
if os.path.exists(font_path):
    # フォントプロパティを作成
    font_prop = fm.FontProperties(fname=font_path)
    # デフォルトのフォントとして設定（あるいは個別に指定も可能）
    plt.rcParams['font.family'] = font_prop.get_name()
    # 【重要】キャッシュを再構築させるための処理が必要な場合があります
    fm.fontManager.addfont(font_path)
    plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()
else:
    st.error(f"フォントファイルが見つかりません: {font_path}")

if os.path.exists(file_path):
    df = pd.read_csv(file_path, index_col='年月')
    # インデックスを日付型に変換する(index_colで年月を指定しているため、インデックスが年月になっている)
    df.index = pd.to_datetime(df.index)
    # インデックスでソートする
    df = df.sort_index()

    st.write('データフレームとして表示した場合')
    st.dataframe(df,column_config={"年月": st.column_config.DatetimeColumn(format="YYYY-MM")})
    st.write('テーブルとして表示した場合')
    st.table(df)
    st.write('折れ線グラフとして表示した場合')
    st.line_chart(df[['平均気温(℃)', '日最高気温の平均(℃)', '日最低気温の平均(℃)']])
    st.write('棒グラフとして表示した場合')
    st.bar_chart(df['降水量の合計(mm)'])
    st.write('matplotlibでグラフを表示した場合')
    fig, ax = plt.subplots()
    ax.plot(df.index, df['平均気温(℃)'])
    ax.set_title('辻堂平均気温の推移', fontproperties=font_prop)
    ax.set_xlabel('年月', fontproperties=font_prop)
    ax.set_ylabel('平均気温(℃)', fontproperties=font_prop)
    st.pyplot(fig)
else:
    # どこを探して失敗したか画面に表示させる（デバッグ用）
    st.error(f"ファイルが見つかりません。検索パス: {file_path}")
    # 念のため、カレントディレクトリの中身を表示して確認
    st.write(f"現在の作業ディレクトリ: {os.getcwd()}")
'''
st.code(code, language='python')

st.subheader('Page_4')
code = '''
import streamlit as st

st.title('参考にしたURLや動画')

video_url = 'https://www.youtube.com/watch?v=4nsTce1Oce8&t=1149s'
st.video(video_url)

st.link_button("Streamlitアプリへのアクセスがモバイル端末からかどうか調べる", "https://qiita.com/ak-sakatoku/items/ebc9d983234ba08b2f00")
'''
st.code(code, language='python')