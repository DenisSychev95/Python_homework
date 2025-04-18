# Вариант с перегрузкой инициализатора Student:
# Возможность создания экземпляра Student c передаваемым в него экземпляром Notebook, созданным извне;
# Возможность создания экземпляра Student с экземпляром Notebook по умолчанию.
class Student:
    def __init__(self, name, notebook=None):
        self.name = name
        self.notebook = notebook if notebook else self.Notebook()

    def __str__(self):
        return f"{self.name} => {self.notebook}"

    class Notebook:
        def __init__(self, model="HP", cpu="i-7", ram=16):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def __str__(self):
            return f"{self.model}, {self.cpu}, {self.ram}"


nb = Student.Notebook()
st1 = Student("Roman", nb)
st2 = Student("Vladimir")
print(st1)
print(st2)

# # Более короткий, но менее гибкий вариант:
# # При создании экземпляра Student сразу создается экземпляр Notebook с параметрами по умолчанию, либо с их передачей;
# # Исключает возможность использования разными экземплярами Student одного и того же экземпляра Notebook.
# class Student:
#     def __init__(self, name, model="HP", cpu="i-7", ram=16):
#         self.name = name
#         self.notebook = self.Notebook(model, cpu, ram)
#         print(f"{self.name} => {self.notebook}")
#
#     class Notebook:
#         def __init__(self, model, cpu, ram):
#             self.model = model
#             self.cpu = cpu
#             self.ram = ram
#
#         def __str__(self):
#             return f"{self.model}, {self.cpu}, {self.ram}"
#
#
# st1 = Student("Roman")
# st2 = Student("Vladimir")