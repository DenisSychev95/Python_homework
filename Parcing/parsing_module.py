# -- coding: utf8 --.
from bs4 import BeautifulSoup
import requests
import re


class Parser:
    page = ""
    data = []

    def __init__(self, url, name):
        self.url = url
        self.name = name

    def get_page(self):
        response = requests.get(self.url).text
        self.page = BeautifulSoup(response, "lxml")

    @staticmethod
    def get_snippet(link):
        response = requests.get(link).text
        page1 = BeautifulSoup(response, "lxml")
        div = page1.find("div", class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
        try:
            p = div.find("p").text.strip()
        except AttributeError:
            p = ""
        return p

    def parsing(self):
        news_list = self.page.find_all("div", class_="tm-article-snippet")
        # print(len(news))
        for news in news_list:
            # название
            title = news.find("h2", class_="tm-title tm-title_h2").text
            # автор
            autor = "https://habr.com" + news.find("a", class_="tm-user-info__username")["href"]
            # ссылка
            link = "https://habr.com" + news.find("h2", class_="tm-title tm-title_h2").find("a")["href"]
            # описание
            snippet = self.get_snippet(link)
            # просмотры
            views1 = news.find("span", class_="tm-icon-counter__value").text
            views2 = re.sub(r"K", "00", views1)
            views = re.sub(r"[.]", "", views2)
            news_info = {"Название": title,
                         "Автор": autor,
                         "Ссылка": link,
                         "Описание": snippet,
                         "Просмотры": views}
            self.data.append(news_info)

    def save_data(self, num):
        with open(self.name, "a", encoding="utf-8") as fw:
            ind = 1
            fw.write(f"Страница: {num}\n")
            for elem in self.data:
                fw.write(f"Новость № {ind}\n\nНазвание :{elem["Название"]}"
                         f"\nАвтор: {elem["Автор"]}\nСсылка: {elem["Ссылка"]}\nОписание: {elem["Описание"]}\n"
                         f"Просмотры: {elem["Просмотры"]}\n\n{"*" * 40}\n")
                ind += 1

    def run_parsing(self):
        self.get_page()
        self.parsing()

