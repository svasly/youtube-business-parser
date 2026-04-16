import googleapiclient.discovery
import pandas as pd
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

# --- НАСТРОЙКИ ---

# Загружаем переменные из файла .env
load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
# Список расширенных запросов для максимального охвата
CATEGORIES = {
    "Юристы и Финансы": [
        "банкротство физических лиц", "юрист москва", "юрист спб", "адвокат", 
        "арбитражный управляющий", "кредитный юрист", "консультация юриста",
        "финансовая грамотность", "личные финансы", "списание долгов"
    ],
    "Недвижимость": [
        "недвижимость москва", "риелтор спб", "новостройки", "купить квартиру", 
        "инвестиции в недвижимость", "обзор жк", "недвижимость сочи",
        "аренда квартир", "загородная недвижимость", "ипотека 2024"
    ]
}

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)
min_date = (datetime.now() - timedelta(days=120)).isoformat() + 'Z' # Последние 4 месяца

def parse_all():
    all_data = []

    for cat_name, keywords in CATEGORIES.items():
        for word in keywords:
            print(f"Ищу по запросу: {word}...")
            next_page_token = None
            pages_per_keyword = 5 # Собираем до 250 результатов на каждое слово

            for page in range(pages_per_keyword):
                try:
                    request = youtube.search().list(
                        q=word,
                        part="snippet",
                        type="video",
                        maxResults=50,
                        regionCode="RU",
                        relevanceLanguage="ru",
                        publishedAfter=min_date,
                        pageToken=next_page_token
                    )
                    response = request.execute()

                    for item in response.get('items', []):
                        all_data.append({
                            'Категория': cat_name,
                            'Название канала': item['snippet']['channelTitle'],
                            # Исправленный формат ссылки
                            'Ссылка': f"https://youtube.com/channel/{item['snippet']['channelId']}",
                            'Дата последнего видео': item['snippet']['publishedAt'],
                            'Описание': item['snippet']['description']
                        })

                    next_page_token = response.get('nextPageToken')
                    if not next_page_token:
                        break
                    
                    # Небольшая пауза, чтобы не злить API
                    time.sleep(0.1) 
                    
                except Exception as e:
                    print(f"Ошибка на запросе {word}: {e}")
                    break

    return all_data

# Запуск
raw_data = parse_all()

# Создаем таблицу и удаляем дубликаты по ссылке на канал
df = pd.DataFrame(raw_data)
if not df.empty:
    df = df.drop_duplicates(subset='Ссылка')
    
    # Сохраняем результат
    output_file = 'youtube_max_base.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\nГотово! Собрано уникальных каналов: {len(df)}")
    print(f"Файл сохранен как: {output_file}")
else:
    print("Ничего не найдено. Проверьте VPN и API ключ.")
