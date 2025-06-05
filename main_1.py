class Animal:
    def __init__(self, name:str, type:str, age:str):

        self.name = name
        self.type = type
        self.age = age

    def animal_sound(self, sound:str, power_sound:str):

        self.sound = sound
        self.power_sound = power_sound

        print(f'Звук животного: {self.sound}\nСила звука животного: {self.power_sound}')



animal = Animal('Мурка', 'Кошка', '7')
print(f'Имя животного: {animal.name}, Вид животного: {animal.type}, Возраст животного: {animal.age}')

animal.animal_sound('sound', '15%')


