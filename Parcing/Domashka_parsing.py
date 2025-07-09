# -- coding: utf8 --.
from parsing_module import Parser


def main():
    for i in range(1, 51):
        pars = Parser(f"https://habr.com/ru/news/page{i}/", "data.txt")
        pars.run_parsing()


if __name__ == "__main__":
    main()
