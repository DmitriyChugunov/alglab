######################## 1 ######################
# class Stusent:
#     def __init__(self, name, age, course, evaluations):
#         self.evaluations = evaluations
#         self.name = name
#         self.age = age
#         self.course =course
#
#     def get_ball(self, evaluations):
#         res = 0
#         for i in evaluations:
#             res += i
#         ball = res / len(evaluations)
#         return ball
#
#     def get_info(self):
#         ball = self.get_ball(self.evaluations)
#         return f'''
# Информация о {self.name}:
#     Возраст: {self.age}
#     Курс: {self.course}
#     Оценки: {self.evaluations}
#     Средний балл: {ball}
#
#
# '''
#
# student1 = Stusent('Дмитрий', '15', '1 курс', [5,4,3,2,5,4,5,1,2,2])
# print(student1.get_info())


######################### 2 #############################

# class rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def perimeter(self):
#         if self.width > self.length:
#             result = (self.width + self.length) * 2
#         else:
#             raise TypeError('Введен не прямоугольник')
#         return print(f'Прямоугольник с шириной {self.width} и высотой {self.length} имеет Периметр : {result}')
#
#     def square(self):
#         if self.width > self.length:
#             result = self.width * self.length
#         else:
#             raise TypeError('Введен не прямоугольник')
#         return print(f'Прямоугольник с шириной {self.width} и высотой {self.length} имеет Площадь : {result}')
#
# v = rectangle(10, 20)
# v.perimeter()
# v.square()

######################### 3 #####################

# class car:
#
#     def __init__(self, make, model, year_of_manufacture,mileage):
#         self.make = make
#         self.model = model
#         self.year_of_manufacture = year_of_manufacture
#         self.mileage = mileage
#
#     def change_make(self, make):
#         self.make = make
#
#     def change_model(self, model):
#         self.model = model
#
#     def change_year_of_manufacture(self, year_of_manufacture):
#         self.year_of_manufacture = year_of_manufacture
#
#     def change_mileage(self, mileage):
#         self.mileage = mileage
#
#     def print_info(self):
#         return print(f"""
# Марка машины: {self.make}
# Модель машины: {self.model}
# Год выпуска: {self.year_of_manufacture}
# Пробег: {self.mileage}
#         """)
#
# car1 = car('LADA', 'Priora', 2009, 237980)
# car1.print_info()
# car1.change_model('4x4')
# car1.print_info()

##################### 4 ##########################


# class Bank:
#     def __init__(self, fio, balance):
#         self.fio = fio
#         self.balance = balance
#         self.history_replenishment = []
#         self.history_withdrawal = []
#
#     def replenishment(self, replenishment_money):
#         self.history_replenishment.append(f'Пополнение счета на сумму {replenishment_money}')
#         self.balance = self.balance + replenishment_money
#         return print(f'Клиент {self.fio} пополнил счет Банка "OOO Чугун" {replenishment_money} рублей, Баланс на данный момент: {self.balance}')
#
#
#     def withdrawal(self ,withdrawal_money):
#         if self.balance >= withdrawal_money:
#             self.history_withdrawal.append(f'Списания со счета на сумму {withdrawal_money}')
#             self.balance = self.balance - withdrawal_money
#             return print(f'Клиент {self.fio} снял из Банка "OOO Чугун" {withdrawal_money} рублей, Баланс на данный момент: {self.balance}')
#         else:
#             return print('На балансе недостаточно средств')
#     def PrintInfo(self):
#         return print(f'''
# Состояние банковского счета {self.fio}:
# Баланс: {self.balance}
# История пополнений: {self.history_replenishment}
# История снятий: {self.history_withdrawal}
# ''')
#
# pol = Bank('Чугунов Дмитрий Александрович', 10000)
# pol.PrintInfo()
# pol.withdrawal(1000)
# pol.PrintInfo()
# pol.replenishment(10000)
# pol.PrintInfo()


################# 5 ##################
import math

class Triangle:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def get_type(self):
        if self.num1 == self.num2 == self.num3:
            return print("Данный треугольник: Равносторонний")
        elif self.num1 == self.num2 or self.num1 == self.num3 or self.num2 == self.num3:
            return print("Данный треугольник: Равнобедренный")
        else:
            return print("Данный треугольник: Разносторонний")

    def get_square(self):
        if self.num1 + self.num2 > self.num3 and self.num1 + self.num3 > self.num2 and self.num2 + self.num3 > self.num1:
            n = (self.num1 + self.num2 + self.num3) / 2
            result = math.sqrt(n * (n - self.num1) * (n - self.num2) * (n - self.num3))
            if math.isnan(result) or result < 0:
                return print('Такого треугольника нету')
            else:
                return print(result)
        return print('Такого треугольника нету')


t1 = Triangle(10, 10, 10)
t2 = Triangle(10, 10, 20)
t3 = Triangle(10, 20, 35)

t1.get_type()
t2.get_type()
t3.get_type()

t1.get_square()
t2.get_square()
t3.get_square()