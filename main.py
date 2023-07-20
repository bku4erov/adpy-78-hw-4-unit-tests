# Задание 1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

for visit in geo_logs.copy():
  if 'Россия' not in [country for city, country in list(visit.values())]:
    geo_logs.remove(visit)

print(geo_logs)

# Задание 2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique_ids = {user_id for user_ids in list(ids.values()) for user_id in user_ids}
print(list(unique_ids))

# Задание 3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

queries_len = [query.count(' ') + 1 for query in queries]
queries_len_distr = {len_val: queries_len.count(len_val) for len_val in set(queries_len)}
queries_count = sum(queries_len_distr.values())
print(*[f'Поисковых запросов из {query_len} слов(а) - {round(queries_len_distr[query_len] / queries_count * 100)}%' for query_len in queries_len_distr], sep='\n')

# Задание 4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_sales = max(stats.values())
# Вывод всех каналов, у которых максимальный объем продаж
print(*[chanel for chanel, sales in stats.items() if sales == max_sales], sep='\n')

# Задание 5
input_list = ['2018-01-01', 'yandex', 'cpc', 100]

if len(input_list) < 2:
  print('Для создания словаря из списка в нем должно быть минимум 2 элемента')
  exit()

dict_from_list = {input_list[-2]: input_list[-1]}
for list_item in reversed(input_list[:-2]):
  dict_from_list = {list_item: dict_from_list}

print(dict_from_list)