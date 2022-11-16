import requests

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

def travel(city):
    return [visit for visit in city for v,k in visit.items() if k[1] == 'Россия']

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def unique_nume(id_list):
    return sorted(list(set([n for user, num in id_list.items() for n in num])))


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def max_stats(stats_max):
    return ''.join(chanal for chanal, rating in stats_max.items() if rating == max(list(stats_max.values())))

#---------------------------------------------------

def ya_folder(token):
    host = 'https://cloud-api.yandex.net'
    headers = {'content-type': 'application/json', 'Authorization': f'OAuth {token}'}
    url = f'{host}/v1/disk/resources'
    params = {'path': '/folder_test/'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code

def ya_del_folder(token):
    host = 'https://cloud-api.yandex.net'
    headers = {'content-type': 'application/json', 'Authorization': f'OAuth {token}'}
    url = f'{host}/v1/disk/resources'
    params = {'path': '/folder_test/'}
    response = requests.delete(url, headers=headers, params=params)

#---------------------------------------------------

