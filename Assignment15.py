# city_infrastructure.py

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {self.owner}")

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

# Demonstration
if __name__ == "__main__":
    # Vehicle demonstration
    car = Vehicle("ABC123", "Sedan", "John Doe")
    bike = Vehicle("XYZ789", "Motorbike", "Jane Smith")

    print(f"Car: {car.registration_number}, Type: {car.type}, Owner: {car.owner}")
    print(f"Bike: {bike.registration_number}, Type: {bike.type}, Owner: {bike.owner}")

    # Update owners
    car.update_owner("Alice Johnson")
    bike.update_owner("Bob Brown")

    # Print updated details
    print(f"Updated Car: {car.registration_number}, Type: {car.type}, Owner: {car.owner}")
    print(f"Updated Bike: {bike.registration_number}, Type: {bike.type}, Owner: {bike.owner}")

    # Event demonstration
    concert = Event("Music Concert", "2024-09-10")

    print(f"Initial Participant Count: {concert.get_participant_count()}")

    # Add participants
    concert.add_participant()
    concert.add_participant()

    # Print updated participant count
    print(f"Updated Participant Count: {concert.get_participant_count()}")
