def find_common_participants(group1, group2, separator=','): # TODO Напишите функцию find_common_participants
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator ='|')
print(common_participants)