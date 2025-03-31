class Automobile:
    def __init__(self, model, year, brand, power, color, price):
        self.model = model
        self.year = year
        self.brand = brand
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.brand}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


test_car = Automobile("X7 M50i", "2021 г.", "BMW", "530 л.с.", "white", "10790000")
test_car.print_info()
# test_car.set_model("Sedan Bakladjan")
# test_car.set_year("1982 г.")
# test_car.set_brand("LaDa")
# test_car.set_power("75 hp")
# test_car.set_color("purple")
# test_car.set_price("50'000 руб.")
# test_car.print_info()
# print(test_car.get_model())
# print(test_car.get_year())
# print(test_car.get_brand())
# print(test_car.get_power())
# print(test_car.get_color())
# print(test_car.get_price())
