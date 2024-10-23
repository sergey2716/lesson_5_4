class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def gp_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('такого этажа не существует')
        else:
            for new_floor in range(new_floor + 1):
                if new_floor < 1:
                    continue
            print(new_floor)

    def __str__(self):
        return f'название: {self.name},количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, other):
        return self + other


    def __iadd__(self, other):

        return self + other
    def __del__(self):
        print (f'Дом в {self.name} снесён,но он останется в истории')

h1 = House('дом 1', 9)
print(House.houses_history)
h2 = House('дом 2', 4)
print(House.houses_history)
h3 = House('дом 3',12)
print(House.houses_history)
del h2
del h3
print(House.houses_history)





