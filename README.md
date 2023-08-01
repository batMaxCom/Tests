# Домашнее задание к лекции 4. «Tests»

### Задача 1. Unit-tests
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» нужно протестировать программу по работе с бухгалтерией из [лекции 2.1](https://github.com/netology-code/py-homework-basic/tree/master/2.1.functions).
Если у вас есть своё решение этой задачи, можно использовать его или использовать предложенный код в директории src этого задания.

* Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
  
Рекомендации по тестам:

1. Если у вас в функциях информация выводилась (print), то теперь её лучше возвращать (return), чтобы можно было протестировать.
2. Input можно «замокать» с помощью ```unittest.mock.patch```. Если с этим будут проблемы, то лучше переписать функции так, чтобы данные приходили через параметры.

### Задача 2. Автотест API Яндекса
Проверим правильность работы Яндекс Диск REST API. Напишите тесты, проверяющие создание папки на Диске.  
Используя библиотеку requests, напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой.

Пример положительных тестов:

* код ответа соответствует 200;
* результат создания папки — папка появилась в списке файлов.

### Задача 3. Не обязательная
Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/.

