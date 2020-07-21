class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
print(flight.passengers)

people = ["amir", "tj", "rohit", "tony"]

for person in people:
    if flight.add_passenger(person):
        print(f"{person} was added")
    else:
        print(f"flight is full {person} could not be added")
        
