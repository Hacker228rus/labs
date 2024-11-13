import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Процесс преобразования файла input.csv"""
    with open(INPUT_FILENAME, 'r') as csv_file:
        dictionary = [row for row in csv.DictReader(csv_file)]

    """Сериализация файла в output.json"""
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
