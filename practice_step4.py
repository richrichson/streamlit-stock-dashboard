import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

# ✅ 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

# 데이터 로딩
df = pd.read_csv("stock_sample.csv")
df['날짜'] = pd.to_datetime(df['날짜'])

# Streamlit UI 구성
st.title("📈 주식 종가 & 거래량 대시보드")

stock_options = df['종목명'].unique()
selected_stock = st.selectbox("종목을 선택하세요", stock_options)

filtered = df[df['종목명'] == selected_stock]

# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(filtered['날짜'], filtered['종가'], color='blue', marker='o')
ax1.set_ylabel("종가 (₩)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.bar(filtered['날짜'], filtered['거래량'], color='gray', alpha=0.3)
ax2.set_ylabel("거래량", color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

plt.title(f"{selected_stock} 종가 + 거래량 추이")
st.pyplot(fig)