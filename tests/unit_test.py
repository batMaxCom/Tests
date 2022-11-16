import unittest
from main import travel, unique_nume, max_stats
from parameterized import parameterized

FIXTURE_1 = [
    ([{'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']}],
    [{'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']}]),
    ([{'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']}],
     []),
    ([{'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']}],
     [{'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']}])
    ]

FIXTURE_2 = [
    ({'user1': [213, 213, 213, 15, 213]},
    [15, 213]),
    ({'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119]},
     [15, 54, 119, 213]),
    ({'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]},
     [15, 35, 54, 98, 119, 213])
]

FIXTURE_3 = [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 55, 'yandex': 20, 'vk': 115}, 'vk'),
    ({'google': 99}, 'google')
]

class TestFunc(unittest.TestCase):

    @parameterized.expand(FIXTURE_1)
    def test_travel(self, city, etalon):
        result = travel(city)
        self.assertEqual(result, etalon)

    @parameterized.expand(FIXTURE_2)
    def test_unique_nume(self, id_list, etalon):
        result = unique_nume(id_list)
        self.assertEqual(result, etalon)

    @parameterized.expand(FIXTURE_3)
    def test_max_stats(self, stats_max, etalon):
        result = max_stats(stats_max)
        self.assertEqual(result, etalon)