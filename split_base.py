import pandas as pd

# 1. Загружаем вашу основную базу
df = pd.read_excel('youtube_max_base.xlsx')

# 2. Фильтруем юристов и убираем бухгалтеров (те самые "минус-слова")
stop_words = ['бухгалтер', 'учет', 'налоги', '1с', 'аудит', 'налогообложение']
lawyers_df = df[df['Категория'] == "Юристы и Финансы"]

# Магия фильтрации: оставляем только тех, где НЕТ стоп-слов в названии и описании
lawyers_df = lawyers_df[~lawyers_df['Название канала'].str.contains('|'.join(stop_words), case=False, na=False)]
lawyers_df = lawyers_df[~lawyers_df['Описание'].str.contains('|'.join(stop_words), case=False, na=False)]

# 3. Выделяем недвижимость
realty_df = df[df['Категория'] == "Недвижимость"]

# 4. Сохраняем в два новых файла
lawyers_df.to_excel('База_Юристы_и_Адвокаты.xlsx', index=False)
realty_df.to_excel('База_Недвижимость.xlsx', index=False)

print(f"Разделение завершено!")
print(f"Юристов (без бухгалтеров): {len(lawyers_df)}")
print(f"Недвижимости: {len(realty_df)}")
