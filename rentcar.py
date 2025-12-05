class Car:
    def __init__(self, car_id, name, rent_price):
        self.car_id = car_id
        self.name = name
        self.rent_price = rent_price
        self.is_rented = False
        self.current_user = None

    def __str__(self):
        status = "Ijara berilgan" if self.is_rented else "Bepul"
        return f"ID: {self.car_id}, Name: {self.name}, Rent Price: {self.rent_price}, Status: {status}"


class User:
    def __init__(self, user_id, name, salary):
        self.user_id = user_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Salary: {self.salary}"


class RentCarService:
    def __init__(self):
        self.cars = []
        self.company_balance = 0

    def add_car(self, car):
        self.cars.append(car)
        print(f"{car.name} mashinasi qo'shildi!")

    def edit_car(self, car_id, name=None, rent_price=None):
        car = self.get_car_by_id(car_id)
        if not car:
            print("Mashina topilmadi!")
            return
        if name:
            car.name = name
        if rent_price:
            car.rent_price = rent_price
        print(f"Mashina {car_id} tahrirlandi!")

    def show_all_cars(self):
        print("Barcha mashinalar:")
        for car in self.cars:
            print(car)

    def show_available_cars(self):
        print("Ijara beriladigan mashinalar:")
        for car in self.cars:
            if not car.is_rented:
                print(car)

    def show_rented_cars(self):
        print("Ijara berilgan mashinalar:")
        for car in self.cars:
            if car.is_rented:
                print(car)

    def rent_car(self, user, car_id):
        car = self.get_car_by_id(car_id)
        if not car:
            print("Mashina topilmadi!")
            return

        if car.is_rented:
            print(f"{car.name} mashinasi hozirda ijarada!")
            return

        if user.salary < car.rent_price:
            print(f"{user.name} ning oyligi yetarli emas!")
            return

        car.is_rented = True
        car.current_user = user
        self.company_balance += car.rent_price
        print(f"{user.name} {car.name} mashinasini ijaraga oldi!")


    def return_car(self, car_id):
        car = self.get_car_by_id(car_id)
        if not car or not car.is_rented:
            print("Mashina ijarada emas yoki topilmadi!")
            return
        print(f"{car.current_user.name} {car.name} mashinasini qaytardi.")
        car.is_rented = False
        car.current_user = None

    def get_car_by_id(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                return car
        return None

user1 = User(1, "Ali", 5000)
user2 = User(2, "Vali", 2000)

car1 = Car(1, "Toyota Camry", 3000)
car2 = Car(2, "Honda Civic", 1500)
car3 = Car(3, "BMW X5", 6000)

service = RentCarService()
service.add_car(car1)
service.add_car(car2)
service.add_car(car3)

service.show_all_cars()
service.show_available_cars()

service.rent_car(user1, 1)  # Ali Toyota Camry oladi
service.rent_car(user2, 1)  # Vali ololmaydi, band
service.rent_car(user2, 3)  # Vali ololmaydi, oyligi yetmaydi

service.show_rented_cars()
service.show_available_cars()

service.return_car(1)
service.show_available_cars()

print(f"Kompaniya balansi: {service.company_balance}")
