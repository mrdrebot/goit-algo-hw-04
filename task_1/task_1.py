from pathlib import Path


def total_salary(path: Path) -> tuple[int, int]:
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            users_list: list = [el.strip().split(",") for el in file.readlines()]

            if not users_list:
                print("У файлі відсутні данні! Перевірте файл!")
                return (0, 0)

            users_dic: dict = {key: float(value) for key, value in users_list}
            total: float = sum(users_dic.values())
            average: float = total / len(users_dic)
            return total, average
    except FileNotFoundError:
        print("Програма не змогла знайти файл!")
        return (0,0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (0,0)
    finally:
        print("Якщо хочете повторити роботу програми, запустіть її заново!")
    
file_path: Path = Path(Path.cwd(), "task_1_data_1.txt")

total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
