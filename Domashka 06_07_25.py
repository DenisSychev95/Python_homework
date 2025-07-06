import requests
from bs4 import BeautifulSoup
import re
import csv
import os


def get_page(url):
    page = requests.get(url).text
    return page


def get_plugins(page):
    soup = BeautifulSoup(page, "lxml")
    plugins = soup.find_all("li", class_="wp-block-post")
    return plugins


def get_title(plugin):
    try:
        title = plugin.find("h3", class_="entry-title").text
    except AttributeError:
        title = ""
    return title


def get_link(plugin):
    try:
        link = plugin.find("h3", class_="entry-title").find("a").get("href")
    except AttributeError:
        link = ""
    return link


def get_rating(plugin):
    try:
        rating = plugin.find("span", class_="rating-count").text
        rating = re.sub(r"\D+", "", rating)
    except AttributeError:
        rating = ""
    return rating


def get_snippet(plugin):
    try:
        snippet = plugin.find("div", {"class": "entry-excerpt"}).text
        snippet = snippet.strip()
    except AttributeError:
        snippet = ""
    return snippet


def write_data(title, link, rating, snippet):
    fieldnames = ["Название", "Ссылка", "Рейтинг", "Описание"]
    data = {fieldnames[0]: title, fieldnames[1]: link, fieldnames[2]: rating, fieldnames[3]: snippet}
    with open("all_plugins.csv", "a") as fw:
        writer = csv.DictWriter(fw, fieldnames=fieldnames, delimiter=";", lineterminator="\r")
        if os.path.getsize("all_plugins.csv") == 0:
            writer.writeheader()
        writer.writerow(data)


def main():
    url = "https://ru.wordpress.org/plugins/"
    page = get_page(url)
    plugins = get_plugins(page)
    for plugin in plugins:
        title = get_title(plugin)
        link = get_link(plugin)
        rating = get_rating(plugin)
        snippet = get_snippet(plugin)
        write_data(title, link, rating, snippet)


if __name__ == "__main__":
    main()
