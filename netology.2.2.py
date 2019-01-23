class Animal:
    name = str()
    fed = 'нет'

    def feed(self):
        if self.fed == 'нет':
            self.fed = 'да'
            print('{} накормлен(а)'.format(self.name))
        else:
            print('{} уже сыт(а)'.format(self.name))

    def listen(self):
        print(self.sound)
        if self.sound == 'Га-га-га':
            print('Это гусь')
        elif self.sound == 'Му-у-у':
            print('Это корова')
        elif self.sound == 'Ме-е-е':
            print('Это овца')
        elif self.sound == 'Ко-ко-ко':
            print('Это курица')
        elif self.sound == 'Бе-е-е':
            print('Это коза')
        elif self.sound == 'Кря-кря':
            print('Это утка')
        else:
            print('Неизвестный зверь')


class Bird:
    eggs = 'Есть'

    def take_eggs(self):
        if self.eggs == 'Есть':
            self.eggs = 'Нет'
            print('Яйца собраны')
        else:
            print('Яиц нет')


class Animal_with_milk:
    milk = 'Есть'

    def get_milk(self):
        if self.milk == 'Есть':
            self.milk = 'Нет'
            print('Молоко получено')
        else:
            print('Молока нет')


class Goose(Animal, Bird):
    type = 'Гусь'
    sound = 'Га-га-га'
    weight = 7


class Chicken(Animal, Bird):
    type = 'Курица'
    sound = 'Ко-ко-ко'
    weight = 2


class Duck(Animal, Bird):
    type = 'Утка'
    sound = 'Кря-кря'
    weight = 3


class Cow(Animal, Animal_with_milk):
    type = 'Корова'
    sound = 'Му-у-у'
    weight = 450


class Goat(Animal, Animal_with_milk):
    type = 'Коза'
    sound = 'Бе-е-е'
    weight = 70


class Sheep(Animal):
    type = 'Овца'
    sound = 'Ме-е-е'
    weight = 75
    wool = 'Есть'

    def get_wool(self):
        if self.wool == 'Есть':
            self.wool = 'Нет'
            print('Шерсть получена')
        else:
            print('Шерсти нет')


goose_1 = Goose()
goose_2 = Goose()
cow = Cow()
sheep_1 = Sheep()
sheep_2 = Sheep()
chicken_1 = Chicken()
chicken_2 = Chicken()
goat_1 = Goat()
goat_2 = Goat()
duck = Duck()


goose_1.name = 'Серый'
goose_2.name = 'Белый'
cow.name = 'Манька'
sheep_1.name = 'Барашек'
sheep_2.name = 'Кудрявый'
chicken_1.name = 'Ко-ко'
chicken_2.name = 'Кукареку'
goat_1.name = 'Рога'
goat_2.name = 'Копыта'
duck.name = 'Кряква'


farm = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]


def work():
    for animal in farm:
        animal.listen()
        animal.feed()
        if hasattr(animal, 'take_eggs'):
            animal.take_eggs()
        if hasattr(animal, 'get_milk'):
            animal.get_milk()
        if hasattr(animal, 'get_wool'):
            animal.get_wool()


def find_heavy_animal():
    heavy_animal = farm[0]
    for animal in farm:
        if animal.weight > heavy_animal.weight:
            heavy_animal = animal
    print('{} самое тяжелое животное на фефрме'.format(heavy_animal.type))


work()
find_heavy_animal()