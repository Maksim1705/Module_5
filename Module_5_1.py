class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
            if 0 < new_floor <=self.number_of_floors:
                for floor in range(1, new_floor +1 ):
                    print(floor)
            else:
                print('Такого этажа несуществует')



h1 = House('ЖК Весна', 18)
h2 = House('Домик на хуторе', 2)
h1.go_to(14)
h2.go_to(3)