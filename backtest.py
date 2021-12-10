import pyupbit
import numpy as np

# ohlcv(open, high, low, close, volumne)
df = pyupbit.get_ohlcv("KRW-BTC", count=7)

# k
df['range'] = (df['high'] - df['low']) * 0.5
# range 컬럼 한칸 씩 밑으로 내림.
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.00
# np.where(조건문, 참일 때 값, 거짓일 때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")