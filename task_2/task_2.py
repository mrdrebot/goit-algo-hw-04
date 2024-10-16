from pathlib import Path 

def get_cats_info(path: Path) -> dict:
    keys_list: list = ["id", "name", "age"]
    with open(path, 'r') as file:
        cats_list: list = [str.strip().split(",") for str in file.readlines()]
        cats_dict: dict = [dict(zip(keys_list, cat)) for cat in cats_list]
        return cats_dict

file_name: str = "task_2_data_3.txt"

try:
    cats_info: dict = get_cats_info(file_name)
    print(cats_info)
except FileNotFoundError:
    print("Програма не змогла знайти файл!")
except (IndexError, ValueError):
    print("Щось не так і даними у файлі! Перевірте дані у файлі!")
finally:
    print("Якщо хочете повторити роботу програми, запустіть її заново!")

'''
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
'''
