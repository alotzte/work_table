import pandas as pd
import numpy as np

# Предположим, что у нас есть следующий DataFrame:
df = pd.read_excel('NeoData.xlsx')

# Применяем функцию, чтобы перенести значения в первую колонку
df['col1'] = df.iloc[:, 1:].apply(lambda row: row.dropna().values[0] if len(row.dropna().values) > 0 else np.nan, axis=1)

# Создаем новый DataFrame, содержащий только первую колонку изначального DataFrame и получившуюся колонку
new_df = pd.DataFrame({
    'Номер': df['Номер'],
    'Разметка': df['col1']
})

# Сохраняем новый DataFrame в CSV-файл
new_df.to_excel('output.xlsx', index=False)
