import pandas as pd
import matplotlib.pyplot as plt
import platform

# ✅ 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

# 📄 데이터 불러오기
df = pd.read_csv("stock_sample.csv")
df['날짜'] = pd.to_datetime(df['날짜'])

# 📊 종가 + 거래량 그래프 함수
def plot_price_and_volume(df, stock_name):
    filtered = df[df['종목명'] == stock_name]

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(filtered['날짜'], filtered['종가'], color='blue', marker='o')
    ax1.set_xlabel("날짜")
    ax1.set_ylabel("종가 (₩)", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.bar(filtered['날짜'], filtered['거래량'], color='gray', alpha=0.3)
    ax2.set_ylabel("거래량", color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    plt.title(f"{stock_name} 종가 + 거래량 추이")
    plt.tight_layout()
    plt.show()

# 실행
plot_price_and_volume(df, "삼성전자")