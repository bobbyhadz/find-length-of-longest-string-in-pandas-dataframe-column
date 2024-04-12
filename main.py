# Pandas: Find length of longest String in DataFrame column

import pandas as pd


df = pd.DataFrame({
    'A': ['A', 'AB', 'ABC'],
    'B': ['BC', 'BCD', 'BCDE'],

})

print(df)

print('-' * 50)

print(df['A'].str.len().max()) # 👉️ 3

print('-' * 50)

print(df['B'].str.len().max()) # 👉️ 4
