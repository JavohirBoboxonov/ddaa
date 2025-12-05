class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"""
Product ID: {self.product_id}
Name: {self.name}
Price: {self.price}
Quantity: {self.quantity}
"""

class User:
    def __init__(self, name, phone_number, password, balance):
        self.name = name
        self.phone_number = phone_number
        self.password = password
        self.__balance = balance
        self.products = []

    @property
    def balance(self):
        return self.__balance

    def update_user_data(self):
        new_name = input("Enter new user name: ")
        new_password = input("Enter new password: ")

        self.name = new_name
        self.password = new_password
        print("Successfully updated user data")
    def my_products(self):
        for product in self.products:
            print(product.get_info())

    def get_info(self):
        return f"""
    Name: {self.name}
    Phone Number: {self.phone_number}
    Password: {self.password}
    """

class Shop:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.products = []
        self.users = []
        self.basket = []

    def add_product(self):
        try:
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            if all(p.product_id != product_id for p in self.products):
                self.products.append(Product(product_id, name, price, quantity))
                print("Product added")
            else:
                print("Product ID already exists!")

        except ValueError as r:
            print(f"Xato {r}")

    def remove_product(self):
        try:
            product_id = int(input("Enter product ID: "))
            for i in self.products:
                if i.product_id == product_id:
                    self.products.remove(i)
        except ValueError:
            print("Error product_id must be intager")
    def update_products(self):
        product_id = int(input("Enter product ID: "))
        for update in self.products:
            if update.product_id == product_id:
                while True:
                    print("1 Mahsulot Nomini O'zgartirish \n2 Mahsulot Narxini O'zgartirish \n3 Mahsulot Miqdorini O'zgartirish \n4 Chiqish")
                    admin_choice = input("Enter Your Choice: ")
                    if admin_choice == "1":
                        new_name = input("Enter new product name: ")
                        update.name = new_name
                    elif admin_choice == "2":
                        new_price = int(input("Enter new product price: "))
                        update.price = new_price
                    elif admin_choice == "3":
                        quantity = int(input("Enter new product quantity: "))
                        update.quantity = quantity
                    elif admin_choice == "4":
                        print("Dastur Tugadi")
                        break
                    else:
                        print("Invalid Choice")
            print("ID topilmadi")
    @property
    def view_company_balance(self):
        return self.__balance
    def update_user_products(self):
        phone_number = input("Enter phone number: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.phone_number == phone_number and user.password == password:
                for product in self.products:
                    print(product.get_info())

    def payment(self, user: User):
        if not self.basket:
            print("Savatcha bo‘sh!")
            return

        total = sum(product.price * product.quantity for product in self.basket)

        print(f"\nTo‘lov summasi: {total}")
        approve = input("To‘lovni amalga oshiraylikmi? (yes/no): ").lower()

        if approve != "yes":
            print("To‘lov bekor qilindi.")
            self.basket.clear()
            print("Savat Bo`shatildi")
            return

        if user.balance >= total:
            user._User__balance -= total
            self.__balance += total
            self.basket.clear()

            print("\nTo‘lov muvaffaqiyatli amalga oshirildi!")
            print(f"Yangi balansingiz: {user.balance}")
        else:
            print("\n Balansingiz yetarli emas!")

    def buy_product(self):
        for product in self.products:
            print(product.get_info())

        try:
            user_input = int(input("Enter product ID: "))
            quantity = int(input("Enter product quantity: "))

            for product in self.products:
                if product.product_id == user_input and product.quantity >= quantity:
                    self.basket.append(Product(product.product_id, product.name, product.price, quantity))
                    product.quantity -= quantity
                    print("Product added to basket")
                    break
            else:
                print("Mahsulot topilmadi")

        except ValueError as r:
            print(f"Xato {r}")

    def view_basket(self):
        for product in self.basket:
            print(product.get_info())

    def view_products(self):
        for product in self.products:
            print(product.get_info())

    def view_all_users(self):
        for user in self.users:
            print(user.get_info())

    def register_user(self):
        try:
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            password = input("Enter your password: ")
            balance = int(input("Enter your balance: "))
            user = User(name, phone_number, password, balance)
            self.users.append(user)
        except ValueError as t:
            print(f"Xato {t}")

    def login_user(self):
        phone_number = input("Enter your phone number: ")
        password = input("Enter your password: ")
        for user in self.users:
            if user.phone_number == phone_number and user.password == password:
                print("\nLogin Successful!\n")

                while True:
                    print("1. Mahsulot Xarid Qilish")
                    print("2. To`lov Qilish")
                    print("3. Savatdagi Mahsulotlarni Ko`rish")
                    print("4. Foydalanuvchi Ma'lumotlarini O`zgartirish")
                    print("5 Hamma Mahsulotlarni Ko`rish")
                    print("6. Chiqish")

                    user_choice = input("Enter Your Choice: ")

                    if user_choice == "1":
                        self.buy_product()

                    elif user_choice == "2":
                        self.payment(user)

                    elif user_choice == "3":
                        self.view_basket()

                    elif user_choice == "4":
                        user.update_user_data()

                    elif user_choice == "5":
                        user.my_products()
                    elif user_choice == "6":
                        print("Chiqildi")
                        break
                    else:
                        print("Noto‘g‘ri tanlov!\n")

                return
        print("Kiritilgan raqam yoki parol noto‘g‘ri!")

    def admin_menu(self):
        while True:
            print("1 Mahsulot qo`shish")
            print("2 Mahsulot O`chirish")
            print("3 Mahsulot Taxrirlash")
            print("4 Mahsulotlarni Ko`rish")
            print("5 Hamma Foydalanuchilarni Ko`rish")
            print("6 Chiqish")
            admin_choice = input("Enter Your Choice: ")
            if admin_choice == "1":
                self.add_product()
            elif admin_choice == "2":
                self.remove_product()
            elif admin_choice == "3":
                self.update_products()
            elif admin_choice == "4":
                self.view_products()
            elif admin_choice == "5":
                self.view_all_users()
            elif admin_choice == "6":
                print("Dastur Tugadi")
                break
            else:
                print("Invalid Choice")
    admin = "login"
    password = "password"

    def main_menu(self):
        while True:
            print("1 Admin Rejimi \n2 Register \n3 Login \n4 Exit")
            choice = input("Enter Your Choice: ")
            if choice == "1":
                login = input("Enter your login: ")
                password = input("Enter your password: ")

                if self.admin == login and self.password == password:
                    self.admin_menu()
            elif choice == "2":
                self.register_user()
            elif choice == "3":
                self.login_user()
            elif choice == "4":
                print("Thank You")
                break
            else:
                print("Invalid Choice")
s1 = Shop("Cola Market", 50000)
s1.main_menu()