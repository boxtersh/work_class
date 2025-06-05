# Задача №1


class Animal:

    def __init__(self, name:str, types:str, age:str):

        self.name = name
        self.types = types
        self.age = age

    def animal_sound(self, sound:str, power_sound:str):

        self.sound = sound
        self.power_sound = power_sound

        print(f'Звук животного: {self.sound}\nСила звука животного: {self.power_sound}')



animal = Animal('Мурка', 'Кошка', '7')
print(f'Имя животного: {animal.name}, Вид животного: {animal.types}, Возраст животного: {animal.age}')

animal.animal_sound('sound', '15%')

print('\033[35m-\033[0m' * 100)
# Задача №2

class book:

    def __init__(self, name_book:str, author_book:str, number_pages:int):

        self.name_book = name_book
        self.author_book = author_book
        self.number_pages = number_pages

    def displaying_book_screen(self):

        print(f'Название книги: {self.name_book}\nАвтор книги: {self.author_book}\nКоличество страниц в книге: {self.number_pages}\n')

    def open_number_pages(self, input_number_pages:str):

        self.input_number_pages = input_number_pages

        while not self.input_number_pages.isdigit():

            print('\033[31mВы ввели не число\033[0m, повторите ввод >> ')
            self.input_number_pages = input('Введите номер страницы которую хотите открыть в данной книге >> ')

        self.input_number_pages = int(self.input_number_pages)

        if self.input_number_pages >= 1 and self.input_number_pages <= self.number_pages:

            print(f'Книга открылась на странице: {self.input_number_pages}')

        else:

            print(f'Книга \033[31mне открылась\033[0m, номер страницы = {self.input_number_pages} \033[31mвыходит за диапазон\033[0m страниц книги от 1 до {self.number_pages}')

book_1 = book('Книга', 'Автор', 275)

book_1.displaying_book_screen()
input_number_pages = input('Введите номер страницы которую хотите открыть в данной книге >> ')
book_1.open_number_pages(input_number_pages)

print('\033[35m-\033[0m' * 100)
# Задача №3

class passenger_plane:

    def __init__(self, manufacturer_plane:str, model_plane:str, quantity_passengers:str):

        self.manufacturer_plane = manufacturer_plane
        self.model_plane = model_plane
        self.quantity_passengers = quantity_passengers

    def displaying_plane(self):

        print(f'Конструкторское бюро: {self.manufacturer_plane}\nМодель самолета: {self.model_plane}\nПассажировместимость: {self.quantity_passengers}')

    def condition_plane(self, height):

        self.height = height
        messege_user = 'Самолет приземлился'

        if height > 0:

            messege_user = 'Самолет взлетел'

        print(messege_user)

    def speed_plane(self, speed = 150):

        self.speed = speed

        print(f'Скорость самолета = {self.speed}')

plane = passenger_plane('Туполев', 'Ту-144', '150' )

plane.displaying_plane()

height = input('Введите высоту самолета 0 или больше 0 >> ')

while not height.isdigit():
    print('\033[31mВы ввели не число, или оно меньше нуля\033[0m, повторите ввод >> ')
    height = input('Введите высоту самолета 0 или больше 0 >> ')

height = int(height)
plane.condition_plane(height)

speed = input('Введите скорость самолета >> ')
while not speed.isdigit():
    print('\033[31mВы ввели не число, или оно меньше нуля\033[0m, повторите ввод >> ')
    speed = input('Введите скорость самолета >> ')

speed = int(speed)
plane.speed_plane(speed)






