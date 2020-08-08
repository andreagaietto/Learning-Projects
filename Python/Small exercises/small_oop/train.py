class Train:

    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __str__(self):
        return str(self.num_cars) + " car train"

    def __len__(self):
        return int(self.num_cars)


a_train = Train(4)
print(a_train)
len(a_train)

