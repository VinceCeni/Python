#Parent Class User
class User:
    name = "Vince"
    email = "splitdesishin@aol.com"
    password = "vince1"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your passcode: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    position = "Associate"

#These invoke the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
    
