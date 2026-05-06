import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

#データ分析関連
st.subheader('データ分析関連')
df = pd.read_csv('./data/辻堂気象データ.csv', index_col='年月')
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
ax.set_title('辻堂平均気温の推移')
# OSに合わせてフォントを自動切り替え
os_name = platform.system()
print(f'OS: {os_name}')
if os_name == 'Darwin':  # Mac
    plt.rcParams['font.family'] = 'Hiragino Sans'
elif os_name == 'Windows':  # Windows
    plt.rcParams['font.family'] = 'MS Gothic'
elif os_name == 'Linux':  # Google Colabなど
    # Linux系でフォントがない場合は別途インストールが必要な場合があります
    plt.rcParams['font.family'] = 'DejaVu Sans'
st.pyplot(fig)