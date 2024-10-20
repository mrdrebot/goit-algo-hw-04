from pathlib import Path 

def get_cats_info(path: Path) -> list:
    keys_list: list = ["id", "name", "age"]
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            cats_list: list = [string.strip().split(",") for string in file.readlines()]
            print(cats_list)
            
            for cat in cats_list:
                if len(cat) != 3:
                    print("У файлі відсутні або некоректні данні!")
                    return []
            
            cats_list_with_keys: list = [dict(zip(keys_list, cat)) for cat in cats_list]
            return cats_list_with_keys
    except FileNotFoundError:
        print("Програма не змогла знайти файл!")
        return []
    finally:
        print("Якщо хочете повторити роботу програми, запустіть її заново!")

file_name: str = "task_2_data_1.txt"

cats_info: list = get_cats_info(file_name)
print(cats_info)
