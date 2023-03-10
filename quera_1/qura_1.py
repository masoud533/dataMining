import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
cnt = 0
for i in range(0, len(np.unique(data.playerId))):
  cnt += 1
print(cnt)
data2 = data
for i in range(0, len(data['playerId'])):
  if data.iloc[i]['outcome'] != 'گُل':
    data2 = data2.drop(index=i)
data2 = data2.groupby('playerId').agg({
    'outcome': 'count',
})
print(data2[data2['outcome'] == data2.max()['outcome']].index.values[0])

data3 = data.groupby('playerId').agg({
    'playType': 'count',
})
data3['outcome'] = data2['outcome']
data3['persent'] = (data2['outcome'] / data3['playType']) * 100
print(f'{data3[data3["persent"] == data3["persent"].max()].index.values[0]},{data3[data3["persent"] == data3["persent"].min()].index.values[0]}')

data4 = data
for i in range(0, len(data['playerId'])):
  if data.iloc[i]['outcome'] in ['مهار توسط دروازه‌بان', 'گُل', 'گُل به‌خودی']:
    data4 = data4.drop(index=i)
print(np.shape(data4))
print(np.shape(data))
des0 = []
for i in range(0 ,len(data4)):
  des0.append(round((((0 - data4.iloc[i]['x']) ** 2) + ((0 - data4.iloc[i]['y']) ** 2)) ** 0.5))
print(max(des0))

