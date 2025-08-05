import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
df = pd.read_csv("stock_sample.csv")
df['날짜'] = pd.to_datetime(df['날짜'])

def plot_price_trend(df, stock_name):
    filtered = df[df['종목명'] == stock_name]

    plt.figure(figsize=(8, 4))
    plt.plot(filtered['날짜'], filtered['종가'], marker='o')
    plt.title(f"{stock_name} 종가 추이")
    plt.xlabel("날짜")
    plt.ylabel("종가 (₩)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_price_trend(df, "삼성전자")