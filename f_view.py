# Декорирующий метод для вывода сообщений на экран(универсальный)
def title(message):
    def wrap(fn):
        def wrapper(*args, **kwargs):
            print(f" {message} ".center(50, "="))
            user_answer = fn(*args, **kwargs)
            print("=" * 50)
            return user_answer
        return wrapper
    return wrap


class UserInterface:
    # Метод выводит приветственное сообщение, запрашивает ввод от пользователя
    @title(" Начало работы приложения ")
    def app_start(self):
        print("Редактирование данных каталога с фильмами:")
        print("1 - добавление фильма\n2 - каталог фильмов\n3 - поиск фильма по названию\n4 - поиск фильма по жанру"
              "\n5 - поиск фильмов по датам выпуска\n6 - поиск фильмов по рейтингу\n7 - поиск фильмов по фильтру"
              "\n8 - просмотр определенного фильма"
              "\n9 - удаление фильма\nq - выход из программы")
        user_input = input("Выберите вариант действия: ").lower().strip()
        return user_input

    # Метод в цикле запрашивает у пользователя информацию о фильме по пунктам:
    # Возвращает словарь ключ(свойства фильма):значение(введенная пользователем информация)
    @title(" Добавление фильма ")
    def show_film_to_add(self):
        # Инициализировали словарь характеристик добавляемого фильма:
        # Ключи словаря на русском языке, значения ключей по умолчанию
        film_dict = {"название фильма": None, "жанр": None, "режиссера": None, "страну производства": None,
                     "год выпуска": None, "длительность фильма": None, "студию": None,
                     "актерский состав": None, "рейтинг фильма": None}
        # В цикле проходим по ключам словаря, пользователь вводит значения, присваиваем значения ключам
        for key in film_dict:
            film_dict[key] = input(f"Введите {key} фильма: ").lower().strip()
        # Возвращаем полученный словарь для передачи его в Controller
        return film_dict

    # Метод выводит сообщение при закрытии приложения
    @title(" Завершение работы приложения ")
    def app_close(self):
        print("Данные успешно сохранены.")

    # Метод выводит сообщение при некорректном выборе варианта действия пользователем
    @title(" Информация об ошибке ")
    def show_incorrect_answer(self, user_answer):
        print(f"Выбранное действие: {user_answer} -  не поддерживается приложением.")

    # Метод принимает каталог(список) содержащий экземпляры класса Film:
    # проходим в цикле по списку с добавлением нумерации при использовании enumerate
    @title(" Просмотр каталога фильмов ")
    def show_film_catalog(self, catalog):
        for ind, film in enumerate(catalog, 1):
            print(f"{ind}) {film}")

    # Метод запрашивает у пользователя название фильма, возвращает название фильма
    @title(" Ввод названия фильма ")
    def get_user_film(self):
        film_title = input("Введите название фильма: ").lower().strip()
        return film_title

    # Метод выводит сообщение об ошибке при вводе пользователем названия фильма, отсутствующего в каталоге
    @title(" Информация об ошибке ")
    def show_incorrect_film_title(self, film_title):
        print(f"Выбранный фильм: {film_title.capitalize()}- отсутствует в каталоге.")

    @title(" Полная информация о фильме ")
    # Метод принимает словарь-экземпляр класса Film, выводит полную информацию о фильме(экземпляре)
    # в отформатированном виде
    def show_user_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    # Метод принимает название фильма и выводит сообщение о его успешном удалении
    @title(" Удаление фильма ")
    def show_removed_film(self, film_title):
        print(f"Фильм {film_title.capitalize()} - был удален.")

    # Запрашивает ключевое из названия фильма у пользователя
    @title(" Поиск по названиям фильмов ")
    def get_user_key_title(self):
        key_film_name = input("Введите ключевое слово названия: ").lower().strip()
        return key_film_name

    # Отображает список подходящих по критерию ключевого слова фильмов
    @title(" Фильмы по ключевому слову ")
    def show_user_key_film_name(self, films):
        if films is None:
            print("По вашему запросу в каталоге ничего не найдено")
        else:
            for ind, film in enumerate(films, 1):
                print(f"{ind}) {film}")

    # Запрашивает у пользователя предпочитаемый жанр(жанры) фильмов
    @title(" Поиск по жанрам фильмов ")
    def get_user_key_genre(self):
        genre_film = input("Введите жанр: ").lower().strip()
        return genre_film

    # Отображает список подходящих по критерию жанра фильмов
    @title(" Фильмы по выбранному жанру ")
    def show_user_genre_films(self, films):
        if films is None:
            print("По вашему запросу в каталоге ничего не найдено")
        else:
            for ind, film in enumerate(films, 1):
                print(f"{ind}) {film}")

    # Запрашивает у пользователя год для начала и окончания поиска фильмов
    @title(" Поиск по запрошенным годам ")
    def get_user_keys_years(self):
        years = []
        year1 = input("Введите год начала поиска: ").lower().strip()
        year2 = input("Введите год окончания поиска: ").lower().strip()
        years.append(year1)
        years.append(year2)
        return years

    # Отображает список подходящих по диапазону поиска фильмов
    @title(" Фильмы за указанный период ")
    def show_user_years_films(self, films):
        if films is None:
            print("По вашему запросу в каталоге ничего не найдено")
        else:
            for ind, film in enumerate(films, 1):
                print(f"{ind}) {film}")

    # Запрашивает у пользователя минимальный рейтинг для поиска фильмов
    @title(" Поиск по рейтингу ")
    def get_user_rating(self):
        rating = input("Введите значение рейтинга от 1 до 9: ").lower().strip()
        return rating

    # Отображает список подходящих по рейтингу фильмов
    @title(" Фильмы по заданному рейтингу ")
    def show_user_rating_films(self, films):
        if films is None:
            print("По вашему запросу в каталоге ничего не найдено")
        else:
            for ind, film in enumerate(films, 1):
                print(f"{ind}) {film}")

    # Запрашивает у пользователя фильтрующие значения: жанр, рейтинг, год
    @title(" Поиск по фильтрам ")
    def get_user_filter(self):
        years = []
        genre = input("Введите жанр: ").lower().strip()
        rating = input("Введите значение рейтинга от 1 до 9: ").lower().strip()
        year1 = input("Введите год начала поиска: ").lower().strip()
        year2 = input("Введите год окончания поиска: ").lower().strip()
        years.append(year1)
        years.append(year2)
        return genre, rating, years

    # Отображает список подходящих по фильтру фильмов
    @title(" Просмотр фильм по фильтру поиска ")
    def show_user_filter_films(self, films):
        if films is None:
            print("По вашему запросу в каталоге ничего не найдено")
        else:
            for ind, film in enumerate(films, 1):
                print(f"{ind}) {film}")