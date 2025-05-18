from .f_model import ModelFilm
from .f_view import UserInterface


class Controller:
    # Инициализатор отрабатывает однократно при создании экземпляра класса в project_films
    def __init__(self):
        # В свойство попадает экземпляр класса ModelFilm из f_model
        self.model_film = ModelFilm()
        # В свойство попадает экземпляр класса UserInterface из f_view
        self.user_interface = UserInterface()

    # Запускает приложение из project_films при обращении к экземпляру Controller
    def start(self):
        # Значение ответа пользователя(по умолчанию) до запуска приложения
        user_answer = None
        while user_answer != "q":
            # Вывод на экран приветственного сообщения для пользователя, получен ответ пользователя
            user_answer = self.user_interface.app_start()
            # Проверка значения полученного ответа пользователя
            self.check_user_answer(user_answer)

    # Метод проверяет приходящее строковое значение, в зависимости от его значения выполняет определенное действие.
    # Запускает соответствующий метод
    def check_user_answer(self, user_answer):
        if user_answer == "1":
            # Запускаем метод show_film_to_add для отображения во View, сохраняем полученные данные в used_added_film
            # used_added_film передается параметром для запуска метода из Model
            user_added_film = self.user_interface.show_film_to_add()
            self.model_film.add_film(user_added_film)
        elif user_answer == "2":
            # Запускаем метод get_film_catalog(), возвращаем список экземпляров класса Film
            catalog = self.model_film.get_film_catalog()
            # Запускаем метод show_film_catalog(catalog), передаем в него полученный список экземпляров класса Film,
            # Проходим в цикле и получаем строковое представление экземпляра класса Film с нумерацией
            self.user_interface.show_film_catalog(catalog)

        elif user_answer == "3":
            key_film_name = self.user_interface.get_user_key_title()
            # Метод, принимает ключевое слово, формирует словарь фильмов по ключевому слову или возвращает None
            films = self.model_film.get_correct_films(key_film_name)
            # Выводим на экран фильмы по ключевому слову
            self.user_interface.show_user_key_film_name(films)

        elif user_answer == "4":
            key_film_genre = self.user_interface.get_user_key_genre()
            films = self.model_film.get_films_genre(key_film_genre)
            self.user_interface.show_user_genre_films(films)

        elif user_answer == "5":
            years = self.user_interface.get_user_keys_years()
            films = self.model_film.get_films_years(years)
            self.user_interface.show_user_years_films(films)
        elif user_answer == "6":
            rating = self.user_interface.get_user_rating()
            films = self.model_film.get_films_rating(rating)
            self.user_interface.show_user_rating_films(films)

        elif user_answer == "7":
            genre, rating, years = self.user_interface.get_user_filter()
            v_rating, v_years = ModelFilm.check_filter_values(rating, years)
            films = self.model_film.get_filter_films(genre, v_rating, v_years)
            self.user_interface.show_user_filter_films(films)

        elif user_answer == "8":
            # Запускаем метод get_user_film(), запрашиваем у пользователя название фильма, возвращаем это название
            film_title = self.user_interface.get_user_film()
            try:
                # Запускаем метод get_single_film(film_title) пробуем найти экземпляр класса Film по ключу film_title
                # в self.films, возвращает отредактированный экземпляр класса Film
                film = self.model_film.get_single_film(film_title)
            except KeyError:
                # Метод отрабатывает в случае исключения KeyError(отсутствие ключа film_title в self.films)
                self.user_interface.show_incorrect_film_title(film_title)
            else:
                # Метод отрабатывает в случае попадания в блок try, выводит полную информацию
                # о передаваемом в метод экземпляре класса Film
                self.user_interface.show_user_film(film)
        elif user_answer == "9":
            # Запускаем метод get_user_film(), запрашиваем у пользователя название фильма, возвращаем это название
            film_title = self.user_interface.get_user_film()
            try:
                self.model_film.remove_user_film(film_title)
            except KeyError:
                # Метод отрабатывает в случае исключения KeyError(отсутствие ключа film_title в self.films)
                self.user_interface.show_incorrect_film_title(film_title)
            else:
                self.user_interface.show_removed_film(film_title)
        # При выходе из программы сохраняем данные в файл
        elif user_answer == "q":
            self.user_interface.app_close()
            self.model_film.save_data()
        else:
            self.user_interface.show_incorrect_answer(user_answer)
