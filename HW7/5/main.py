# импортируем библиотеку для работы с данными pandas as pd
import pandas as pd

# Читаем и сохраняем содержимое excel файла
read_file = pd.read_excel("Test.xlsx")

# Записываем объект с данными в csv файл
read_file.to_csv("Test.csv",
                 index=None,
                 header=True)

# Читаем csv файл и преобразуем в объект данных
df = pd.DataFrame(pd.read_csv("Test.csv"))

# Отображаем объект с данными
print(df)
