import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from pathlib import Path

#データ分析関連
st.title('データ分析の例')

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

    st.subheader('データフレームとして表示した場合')
    st.dataframe(df,column_config={"年月": st.column_config.DatetimeColumn(format="YYYY-MM")})

    st.subheader('テーブルとして表示した場合')
    st.table(df)

    st.subheader('折れ線グラフとして表示した場合')
    st.line_chart(df[['平均気温(℃)', '日最高気温の平均(℃)', '日最低気温の平均(℃)']])

    st.subheader('棒グラフとして表示した場合')
    st.bar_chart(df['降水量の合計(mm)'])

    st.subheader('matplotlibでグラフを表示した場合')
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

