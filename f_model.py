import os
import pickle
import re


class Film:
    # При создании экземпляра класса Film запрашивает значение ключей
    def __init__(self, title, genre, director, country, year, duration, studio, actors, rating):
        self.title = title
        self.genre = genre
        self.director = director
        self.country = country
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors
        self.rating = rating

    # Строковое представление для экземпляра класса Film
    def __str__(self):
        return (f"Название фильма: {self.title.capitalize()}; жанр: {self.genre}; "
                f"выпуск фильма в прокат: {self.year}г")

    def format_rating(self):
        try:
            f_rating = int(self.rating)
        except ValueError:
            f_rating = "неизвестно"
        else:
            f_rating = f_rating / 10
        return f_rating

    def format_duration(self):
        try:
            f_duration = int(self.duration)
        except ValueError:
            f_duration = "неизвестно"
        else:
            duration_hours = str(f_duration // 60)
            duration_min = str(f_duration % 60)
            duration_str = f" / {duration_hours}ч:{duration_min}мин"
            f_duration = str(f_duration) + " мин" + duration_str
        return f_duration

    def format_year(self):
        pattern = r"19[3-9][\d]|200[\d]|201[\d]|202[0-5]"
        value = len(re.findall(pattern, self.year))
        f_year = self.year
        if f_year.isdigit():
            if value == 1:
                f_year = self.year + "г"
        else:
            f_year = "неизвестно"
        return f_year

    def format_country(self):
        f_country = self.country.title()
        if "Сша" in f_country:
            f_country = re.sub("Сша", "США", f_country)
        if "Usa" in f_country:
            f_country = re.sub("Usa", "USA", f_country)
        return f_country


class ModelFilm:
    def __init__(self):
        self.data_filename = "films.txt"
        # При создании экземпляра класса ModelFilm запускает метод load_data:
        # Присваивает в свойство возвращенное значение
        self.films = self.load_data()

    # Метод считывания данных из файла, возвращает данные. Если файл не существует, возвращает {}
    def load_data(self):
        if os.path.exists(self.data_filename):
            with open(self.data_filename, "rb") as fr:
                data = pickle.load(fr)
                return data
        else:
            return {}

    # Метод записывает данные в файл с использованием модуля pickle, в self.films находится словарь:
    # Структура словаря {{"значение свойства self.title экземпляра класса Film": экземпляр класса Film}, ...}
    def save_data(self):
        with open(self.data_filename, "wb") as fw:
            pickle.dump(self.films, fw)

    # Метод принимает словарь film_dict, переданный в Controller, создает экземпляр класса Film
    def add_film(self, film_dict):
        # При создании экземпляра класса, в параметры передаем распакованные значения film_dict
        film = Film(*film_dict.values())
        # В свойство self.films добавляем словарь:
        # {{"значение свойства self.title экземпляра класса Film": экземпляр класса Film}, ...}
        self.films[film.title] = film

    # Метод возвращает только значения свойства self.films- экземпляры класса Film
    def get_film_catalog(self):
        return self.films.values()

    # Метод принимает название фильма(ключ свойства self.films), возвращает значение ключа self.films[film_title]:
    # Экземпляр класса Film, возвращает словарь
    def get_single_film(self, film_title):
        film = self.films[film_title]
        film_dict = {"Название фильма": film.title.capitalize(), "Жанр": film.genre,
                     "Режиссер": film.director.title(), "Страна производства": film.format_country(),
                     "Год выпуска": film.format_year(), "Длительность фильма": film.format_duration(),
                     "Студия": film.studio.capitalize(), "Актеры": film.actors.title(), "Рейтинг": film.format_rating()}
        return film_dict

    # Метод принимает название фильма(ключ свойства self.films), удаляет ключ film_title и возвращает имя ключа
    def remove_user_film(self, film_title):
        return self.films.pop(film_title)

    # Принимает ключевое слово, ищет названия фильмов по ключевому слову, словарь подходящих фильмов или None
    def get_correct_films(self, key):
        # Список ключей self.films
        lst_keys = []
        dict_films = {}
        films = self.films.items()
        keys_films = self.films
        for name in keys_films:
            if key in name:
                lst_keys.append(name)
        if len(lst_keys) != 0:
            for key, value in films:
                if key in lst_keys:
                    dict_films[key] = value
            dict_films = dict_films.values()
        else:
            dict_films = None
        return dict_films

    # Принимает жанр, производит поиск по фильмам, если совпадения по жанру находятся, фильм добавляется в список:
    # Возвращает список экземпляров Film или None
    def get_films_genre(self, genre):
        films_genre = []
        for value in self.films.values():
            if genre in value.genre:
                films_genre.append(value)
        if len(films_genre) != 0:
            films = films_genre
        else:
            films = None
        return films

    # Принимает список с двумя датами, производит поиск по фильмам: если год выпуска попадает в диапазон:
    # Фильм добавляется в список:
    # Возвращает список экземпляров Film или None
    def get_films_years(self, years):
        films_years = []
        try:
            years_int = list(map(int, years))
        except ValueError:
            films = None
        else:
            for value in self.films.values():
                try:
                    year = int(value.year)
                except ValueError:
                    continue
                else:
                    if years_int[0] <= year <= years_int[1]:
                        films_years.append(value)
            if len(films_years) != 0:
                films = films_years
            else:
                films = None
            return films

    # Принимает значение рейтинга, производит поиск по фильмам: если рейтинг фильма соответствует:
    # Фильм добавляется в список:
    # Возвращает список экземпляров Film или None
    def get_films_rating(self, rating):
        films_rating = []
        try:
            rating_int = int(rating)
        except ValueError:
            films = None
        else:
            for value in self.films.values():
                try:
                    rating = int(value.rating) / 10
                except ValueError:
                    continue
                else:
                    if rating_int <= rating:
                        films_rating.append(value)
            if len(films_rating) != 0:
                films = films_rating
            else:
                films = None
            return films

    # Метод принимает введенное значения: рейтинг, годы, проверяет, возвращает корректные значения или None
    @staticmethod
    def check_filter_values(rating, years):
        try:
            rating = int(rating)
            years = list(map(int, years))
        except ValueError:
            rating = None
            years = None
        return rating, years

    # Принимает жанр, рейтинг, список дат; производит поиск по фильмам: если все условия соответствуют:
    # Фильм добавляется в список:
    # Возвращает список экземпляров Film или None
    def get_filter_films(self, genre, rating, years):
        filter_films = []
        if (rating, years) is None:
            films = None
        else:
            for value in self.films.values():
                try:
                    f_rating = int(value.rating) / 10
                    year = int(value.year)
                except ValueError:
                    continue
                else:
                    if genre in value.genre and years[0] <= year <= years[1] and rating <= f_rating:
                        filter_films.append(value)
                        if len(filter_films) != 0:
                            films = filter_films
                        else:
                            films = None
                        return films
