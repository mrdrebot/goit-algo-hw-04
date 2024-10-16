from pathlib import Path

def total_salary(path: Path) -> tuple[int, int]:
    with open(path, 'r', encoding = 'utf-8') as file:
        users_list: list = [el.strip().split(",") for el in file.readlines()]

        if not users_list:
            return ()

        users_dic: dict = {key: int(value) for key, value in users_list}
        total: int = sum(users_dic.values())
        average: int = total // len(users_dic)
        return total, average
    
file_path: Path = Path(Path.cwd(), "task_1_data_1.txt")

try:
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError:
    print("Програма не змогла знайти файл!")
except (IndexError, ValueError):
    print("Щось не так і даними у файлі! Перевірте дані у файлі!")
finally:
    print("Якщо хочете повторити роботу програми, запустіть її заново!")
