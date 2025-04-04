class Converter:
    def __init__(self, weight=0):
        self.__weight = weight

    @staticmethod
    def __check_value(value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    @property
    def weight(self):
        return f"{self.__weight} кг => {round((self.convert()), 3)} фунтов"

    @weight.setter
    def weight(self, weight):
        if Converter.__check_value(weight):
            self.__weight = weight
        else:
            print("Килограммы задаются только числами")

    @weight.deleter
    def weight(self):
        del self.__weight

    def convert(self):
        return self.__weight * 2.205


p1 = Converter()
# print(p1.weight)
p1.weight = 12
print(p1.weight)
p1.weight = 41
print(p1.weight)
p1.weight = "двенадцать"
# del p1.weight