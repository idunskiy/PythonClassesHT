class Vehicle:
    def __init__(self, type, model, engine_size):
        self.type = type
        self.model = model
        self.engine_size = engine_size

    def __str__(self):
        return f'Type of a vehicle is {self.type}, model is {self.model} and engine size is {self.engine_size}'


class Train(Vehicle):
    average_wagon_weight = 26

    def __init__(self, type, model, engine_size, wagons_count):
        super(Train, self).__init__(type, model, engine_size)
        self.wagons_count = wagons_count

    def train_mass(self):
        print (f'Mass of this train is {self.average_wagon_weight*self.wagons_count} tons')


class Plane(Vehicle):

    def __init__(self, type, model, engine_size, seats_max):
        super(Plane, self).__init__(type, model, engine_size)
        self.seats_max = seats_max

    def are_free_seats(self, seats_number):
        if seats_number > self.seats_max:
            print(f'There are no free seats in {self.model} airplane')
        else:
            print(f'There are {self.seats_max-seats_number} free seats in {self.model} airplane')


train = Train('High-speed train', 'KW-34', 42, 30)
train.train_mass()

plane = Plane('Passenger plane', 'Boeing 737 Max 7', 300, 172)
plane.are_free_seats(100)
