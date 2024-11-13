import json

def task() -> float:
    """открытие файла input.json"""
    with open('input.json') as f:
        data = json.load(f)
        total_sum = 0
        for line in data:
            multiplier = line['score'] * line['weight']
            total_sum += multiplier
    round_summ = round(total_sum, 3)
    return round_summ


print(task())
