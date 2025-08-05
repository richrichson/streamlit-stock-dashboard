import pandas as pd

def filter_by_price(df, min_price):
    filtered = df[df['종가'] >= min_price]
    return filtered.sort_values(by='종가', ascending=False)

df = pd.read_csv("stock_sample.csv")

min_price = int(input("필터링할 최소 종가를 입력하세요: "))

print(filter_by_price(df, min_price))