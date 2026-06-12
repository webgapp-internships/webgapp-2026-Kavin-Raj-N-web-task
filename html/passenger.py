class passenger_details:

    def __init__(self, passenger_name, ticket_price):
        self.passenger_name = passenger_name
        self.ticket_price = ticket_price

    def details(self):
        print("Passenger Name: ", self.passenger_name)
        print("Ticket Price: ", self.ticket_price)
        print()


passengers_list = (
    passenger_details("Alice", 200),
    passenger_details("Bob", 400),
    passenger_details("Charlie", 300),
    passenger_details("Diana", 250),
)

for i in passengers_list:
    i.details()

j = 0
collection = 0

while j < len(passengers_list):
    collection += passengers_list[j].ticket_price
    j+=1
print("Total Collection: ", collection)
