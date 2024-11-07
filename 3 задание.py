def count_letters(text):
    letter_count = {}
    text = text.lower()  # Приводим текст к нижнему регистру

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count


def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())  # Общее количество букв
    frequency = {}

    for letter, count in letter_count.items():
        frequency[letter] = round(count / total_letters, 2)  # Вычисляем частоту и округляем

    return frequency


def print_frequencies_in_order(text):
    letter_count = count_letters(text)
    frequency = calculate_frequency(letter_count)

    # Печатаем результаты в порядке появления букв в тексте
    printed = set()  # Множество для отслеживания уже напечатанных букв
    for char in text.lower():
        if char.isalpha() and char not in printed:
            printed.add(char)  # Добавляем букву в множество
            print(f"{char}: {frequency[char]}")

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
print_frequencies_in_order(main_str)
