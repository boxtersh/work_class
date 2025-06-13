# Задача №1


class Animal:

    def __init__(self,
                 name:str,
                 types:str,
                 age:str
    ):

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

class Book:

    def __init__(self,
                 name_book:str,
                 author_book:str,
                 number_pages:int
    ):

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

book_1 = Book('Книга', 'Автор', 275)

book_1.displaying_book_screen()
input_number_pages = input('Введите номер страницы которую хотите открыть в данной книге >> ')
book_1.open_number_pages(input_number_pages)

print('\033[35m-\033[0m' * 100)
# Задача №3

class Passenger_plane:

    def __init__(
            self,
            manufacturer_plane:str,
            model_plane:str,
            quantity_passengers:str,
            current_height: int,
            current_speed: int
    ):

        self.manufacturer_plane = manufacturer_plane
        self.model_plane = model_plane
        self.quantity_passengers = quantity_passengers
        self.current_height = current_height
        self.current_speed = current_speed

    def __str__(self):

        return (f'Конструкторское бюро: {self.manufacturer_plane}\n'
                f'Модель самолета: {self.model_plane}\n'
                f'Пассажировместимость: {self.quantity_passengers}\n'
                f'Текущая высота: {self.current_height}\n'
                f'Текущая скорость: {self.current_speed}\n')

    def validate_input_int(self, height, speed):

        if height.isdigit() and speed.isdigit():
            height = int(height)
            speed = int(speed)

            if height <= 20000 and speed <= 2500:
                return height, speed, False

            else:
                height = self.current_height
                speed = self.current_speed
                return height, speed, True

        else:
            height = self.current_height
            speed = self.current_speed
            return height, speed, True



    def current_position_aircraft(self):

        print(f'Характеристики самолета сейчас высота/скорость:\n'
              f'Текущая высота: {self.current_height}\n'
              f'Текущая скорость: {self.current_speed}\n\n'
              f'Введите текущие характеристики самолета высота/скорость:\n'
              f'Примечание:\nНа земле (высота = 0м) скорость должна быть 0 <= speed <= 250\n'
              f'На высоте (0 < высота <= 350м) скорость должна быть 250 < speed <= 300\n'
              f'На высоте (350 < высота <= 2000м) скорость должна быть 300 < speed <= 500\n'
              f'На высоте (2000 < высота < 20000) скорость должна быть 500 < speed <= 2500\n\n')

        height = input('Введите высоту полета самолета >> ')
        speed = input('Введите скорость самолета >> ')
        height, speed, boll = self.validate_input_int(height,speed)

        while boll:
            print(f'''Введено неверное значение (не число, число отрицательно, число дробно,'
                  f'для скорости значение введено больше 2500)'
                  f'для высоты значение введено больше 20000\n''')
            height = input('Введите высоту полета самолета  >> ')
            speed = input('Введите скорость полета самолета >> ')
            height, speed, boll = self.validate_input_int(height, speed)

        early_height = self.current_height
        early_speed = self.current_speed
        flag = False

        if height == 0:

            if speed >= 0 and speed <= 250:
                self.current_height = height
                self.current_speed = speed
                return early_height, early_speed, flag

            else:
                print('Несоответствие введенных данных высота/скорость\n')
                return early_height, early_speed, flag

        elif height > 0 and height <= 350:

            if speed > 250 and speed <= 300:
                self.current_height = height
                self.current_speed = speed
                return early_height, early_speed, flag

            else:
                print('Несоответствие введенных данных высота/скорость\n')
                return early_height, early_speed, flag

        elif height > 350 and height <= 2000:

            if speed > 300 and speed <= 500:
                self.current_height = height
                self.current_speed = speed
                return early_height, early_speed, flag

            else:
                print('Несоответствие введенных данных высота/скорость\n')
                return early_height, early_speed, flag

        else:

            if speed > 500 and speed <= 2500:
                self.current_height = height
                self.current_speed = speed
                return early_height, early_speed, flag

            else:
                print('Несоответствие введенных данных высота/скорость\n')
                return

    def flight_status(self, early_height: int, early_speed: int, flag: bool):

        status_height = ''
        status_speed = ''
        if flag:
            if self.current_height == 0:
                print(f'Самолет на земле:\nвысота - {self.current_height}\n'
                      f'скорость - {self.current_speed}\n')

            else:
                print(f'Самолет в воздухе:\nвысота - {self.current_height}\n'
                      f'скорость - {self.current_speed}\n')
        else:
            if early_height == self.current_height:
                status_height = 'Без изменений высоты полета самолета'

            if early_height < self.current_height and early_height == 0:
                status_height = 'Самолет взлетел'

            elif early_height < self.current_height and early_height != 0:
                status_height = 'Самолет увеличил высоту'

            elif early_height > self.current_height and self.current_height == 0:
                status_height = 'Самолет приземлился'

            elif early_height > self.current_height and self.current_height != 0:
                status_height = 'Самолет снизил высоту'

            elif early_speed == self.current_speed:
                    status_speed = 'Без изменений скорости самолета'

            elif early_speed < self.current_speed and early_speed == 0:
                status_speed = 'Самолет начал разгон'

            elif early_speed < self.current_speed and early_speed != 0:
                status_speed = 'Самолет увеличил скорость'

            elif early_speed > self.current_speed and self.current_speed == 0:
                status_speed = 'Самолет остановился'

            elif early_speed > self.current_speed and self.current_speed != 0:
                status_speed = 'Самолет снизил скорость'

            print(f'{status_height}\n{status_speed}')


        print()

    def changing_height_plane(self):

        early_height = self.current_height
        early_speed = self.current_speed
        speed = str(self.current_speed)
        height = input('Введите высоту полета самолета >> ')
        height, speed, boll = self.validate_input_int(height, speed)

        while boll:

            print(f'Введено неверное значение (не число, число отрицательно, число дробно,'
                  f'или для высоты полета значение введено больше 20000км)\n')
            height = input('Введите высоту полета самолета >> ')
            speed = str(self.current_speed)
            height, speed, boll = self.validate_input_int(height, speed)

        if self.current_speed >= 0 and self.current_speed <= 250:

            if  height == 0:
                self.current_height = height
                return early_height, early_speed, False

            else:
                print(f'Неверное значение высоты. Скорость самолета = {self.current_speed}км/ч, '
                      f'на такой скорости самолет находиться на земле, может быть:\n'
                      f'- готовится к взлету или на стоянке (скорость = 0км/ч)\n'
                      f'- взлетает или садится\n\n')

                return early_height, early_speed, True

        elif self.current_speed > 250 and self.current_speed <= 300:

            if  height > 0 and height <= 350:
                self.current_height = height
                return early_height, early_speed, False

            else:
                print(f'Неверное значение высоты. Скорость самолета = {self.current_speed}км/ч, '
                      f'на такой скорости самолет находится в полете:\n'
                      f'- совершает взлет или посадку\n\n')
                return early_height, early_speed, True

        elif self.current_speed > 300 and self.current_speed <= 500:

            if  height > 350 and height <= 2000:
                self.current_height = height
                return early_height, early_speed, False

            else:
                print(f'Скорость самолета = {self.current_speed}км/ч, на такой скорости'
                      f'самолет может находиться на высоте 350 < высота <= 2000м')
                return early_height, early_speed, True

        elif self.current_speed > 500 and self.current_speed <= 2500:

            if height > 2000 and height <= 20000:
                self.current_height = height
                return early_height, early_speed, False

            else:
                print(f'Скорость самолета = {self.current_speed}км/ч, на такой скорости'
                      f'самолет может находиться на высоте 2000 < высота <= 20000м')
                return early_height, early_speed, True

        else:
            print('Неверно указана высота')
            return early_height, early_speed, True

    def changing_speed_plane(self):

        early_height = self.current_height
        early_speed = self.current_speed
        height = str(self.current_height)
        speed = input('Введите скорость самолета >> ')
        height, speed, boll = self.validate_input_int(height, speed)

        while boll:

            print(f'Введено неверное значение (не число, число отрицательно, число дробно,'
                  f'или для скорости значение введено больше 2500км/ч)')
            speed = input('Введите скорость самолета >> ')
            height = str(self.current_height)
            height, speed, boll = self.validate_input_int(height, speed)

        if self.current_height == 0:

            if  speed >= 0 and speed <= 250:
                self.current_speed = speed
                return early_height, early_speed, False

            else:
                print(f'Самолет на земле, введенная скорость не может быть больше '
                      f'взлетно-посадочной скорости > 250км/ч')
                return early_height, early_speed, True

        elif self.current_height > 0 and self.current_height <= 350:

            if  speed > 250 and speed <= 300:
                self.current_speed = speed
                return early_height, early_speed, False

            else:
                print(f'Самолет на высоте = {self.current_height}, введенная скорость может быть '
                      f'> 250 или <= 300км/ч')
                return early_height, early_speed, True

        elif self.current_height > 350 and self.current_height <= 2000:

            if  speed > 300 and speed <= 500:
                self.current_speed = speed
                return early_height, early_speed, False

            else:
                print(f'Самолет на высоте = {self.current_height}, введенная скорость может быть '
                      f'> 300 или <= 500км/ч')
                return early_height, early_speed, True


        elif self.current_height > 2000 and self.current_height < 20000:

            if  speed > 500 and speed <= 2500:
                self.current_speed = speed
                return early_height, early_speed, False

            else:
                print(f'Самолет на высоте = {self.current_height}, введенная скорость может быть '
                      f'> 500 или <= 2500км/ч')
                return early_height, early_speed, True

        else:
            print(f'Неверно введена скорость самолета')
            return early_height, early_speed, True


def menu_plane():
    print(f'1: Информация о самолете\n'
          f'2: Ввод текущего положения самолета высота/скорость\n'
          f'3: Изменение текущей высоты\n'
          f'4: Изменение текущей скорости\n'
          f'5: Текущее положение самолета\n'
          f'6: Меню\n'
          f'7: Выход\n')

plane = Passenger_plane('Туполев', 'Ту-144', '150', 0, 0 )
menu_plane()
early_height = 0
early_speed = 0
flag = True

while True:
    result = input('Выберете пункт меню >> ')
    match result:
        case '1':
            print(plane)
            print()

        case '2':
            early_height, early_speed, flag = plane.current_position_aircraft()

            plane.flight_status(early_height, early_speed, flag)

        case '3':
            early_height, early_speed, flag = plane.changing_height_plane()
            plane.flight_status(early_height, early_speed, flag)

        case '4':
            early_height, early_speed, flag = plane.changing_speed_plane()
            plane.flight_status(early_height, early_speed, flag)

        case '5':
            plane.flight_status(early_height, early_speed, True)

        case '6':
            menu_plane()

        case '7':
            break

print('\033[35m-\033[0m' * 100)
# Задача №4

class MusicAlbum:

    def __init__(self,
                 performer = 'Ария',
                 name_music_album = '1100',
                 genre_music = 'Рок',
                 list_music_tracks = ['Песня_1', 'Песня_2', 'Песня_3']
    ):

        self.performer = performer
        self.name_music_album = name_music_album
        self.genre_music = genre_music
        self.list_music_tracks = list_music_tracks

    def __str__(self):

        if self.list_music_tracks == []:

            return (f'\nИсполнитель: {self.performer}\nНазвание альбома: {self.name_music_album}\n'
                f'Музыкальный жанр: {self.genre_music}\nТрек лист: трек лист пуст\n')

        else:
            return (f'\nИсполнитель: {self.performer}\nНазвание альбома: {self.name_music_album}\n'
                f'Музыкальный жанр: {self.genre_music}\nТрек лист: {', '.join(self.list_music_tracks)}\n')

    def displaying_track_list(self):

        print(f'\nТреки в музыкальном альбоме:\n№п/п Песня\n{'-'* 12}')
        for i in range(len(self.list_music_tracks)):

            print(f'{i + 1}: {self.list_music_tracks[i]}')


    def add_tracks(self):

        result = input('Желаете добавить трек в альбом? y / n >> ')

        if result == 'y':

            name_song = input('Введите название песни >> ')
            if name_song in self.list_music_tracks:

                result = input('Данная композиция существует в трек листе, желаете добавить? y / n >> ')
                if result == 'y':

                    self.list_music_tracks.append(name_song)
                    print(music_album)
                    return

            else:
                self.list_music_tracks.append(name_song)
                print(music_album)
                return

        elif result == 'n':
            return

        else:
            print(f'Неверный ввод y / n\n')

    def del_tracks(self):

        result = input('Желаете удалить трек из альбома? y / n >> ')

        if result == 'y':
            self.displaying_track_list()
            name_song_or_number = input('Введите порядковый номер или название песни >> ')

            for i in range(len(self.list_music_tracks)):

                if name_song_or_number == str(i+1):
                    del self.list_music_tracks[i]
                    self.displaying_track_list()
                    return

                elif name_song_or_number == self.list_music_tracks[i]:
                    self.list_music_tracks.remove(name_song_or_number)
                    self.displaying_track_list()
                    return

            print(f'Указанная песня или порядковый номер не найден\n')
            return

        elif result == 'n':
            return

        else:
            print(f'Неверный ввод y / n\n')

    def play_song(self):

        result = input('Желаете воспроизвести музыкальный трек из альбома? y / n >> ')

        if result == 'y':
            self.displaying_track_list()
            name_song_or_number = input('Введите порядковый номер или название песни которую хотите включить >> ')

            for i in range(len(self.list_music_tracks)):

                if name_song_or_number == str(i+1):
                    print(f'Воспроизводится трек: {self.list_music_tracks[i]}\n')
                    return

                elif name_song_or_number == self.list_music_tracks[i]:
                    print(f'Трек {name_song_or_number} включен')
                    return

            print(f'Указанная песня или порядковый номер не найден\n')
            return

        elif result == 'n':
            return

        else:
            print(f'Неверный ввод y / n\n')



music_album = MusicAlbum()
print(music_album)
music_album.add_tracks()
music_album.del_tracks()
music_album.play_song()



