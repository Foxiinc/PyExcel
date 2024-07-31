import pandas as pd
import os

def load_file(file_path):
    # Проверяем расширение файла
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension == '.csv':
        # Загружаем CSV файл
        data = pd.read_csv(file_path)
    elif file_extension in ['.xls', '.xlsx']:
        # Загружаем Excel файл
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type: {}".format(file_extension))
    
    return data

def extract_data(data, row_index, column_index):
    # Извлекаем строку и столбец по заданным индексам
    line = data.iloc[row_index].tolist()
    column = data.iloc[:, column_index].tolist()
    
    return line, column

# Пример использования
file_path = input("Введите путь к файлу (Excel или CSV): ")

try:
    data = load_file(file_path)
    
    # Указываем индексы строки и столбца для извлечения
    row_index = int(input("Введите индекс строки (начиная с 0): "))
    column_index = int(input("Введите индекс столбца (начиная с 0): "))
    
    line, column = extract_data(data, row_index, column_index)
    
    print("Извлеченная строка:")
    print(line)
    
    print("\nИзвлеченный столбец:")
    print(column)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
