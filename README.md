# Проект X

## Описание:

Проект X - это веб-приложение на Python для управления задачами и проектами.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте модуль main.py в корне проекта.
2. в качестве параметров передайте 2 сроки (user - По какому слову в описании или категории будем искать?
   а так же: user_2 - По какой категории будем искать?).
3. В консоли проекта будет виден результат выполнения работы проекта.


## Функции:

Модуль utils.py:
   * hello_date - функция генерирующая словарь с приветствием в зависимости от времени суток.
   * read_file - функция читающая файл в excel формате и возвращающая список словарей.
   * return_cash - функция АПИ возвращает курс валют списком.
   * return_invest - функция АПИ возвращает 5 акций из списка SP&F500.
   * card-info - функция, которая "обрезает" информацию полученную при чтении excel файла до списка словарей нужного вида.
   * top_5 - функция, которая выводит топ 5 транзакций в виде списка словарей.
Модуль views.py:
   * main_str - функция, которая собирает результаты работы модуля utils в единый json-файл, в том числе 
      за счет декоратора reports.
Модуль services.py:
   * simpl_search - функция осуществляет простой поиск по категориям или описанию списка словарей.
Модуль reports.py:
   * Декоратор reports - обернув в который функцию можно преобразовать результат ее работы в json-файл.
   * category_by_date - функция поиска по категориям предложенного списка словарей, по дате, по умолчанию, в качестве 
      даты, передается сегодняшняя дата и возвращается список словарей с транзакциями за 3 месяца от указанной даты.
Модуль main.py:
   * main - главная функция проекта, в которой объединены в единый словарь результаты выведения страниц: 
   главная, сервисы и отчеты. Для удобства формирования json-ответа фронтенду.

## Тестирование:

Покрытие проекта тестами не менее 80% (98%). Все тесты запускаются из терминала через pytest.

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).