import random
import csv

with open("demo.csv","a") as i:
    pass

fieldnames = ['number', 'name', 'password', "balance"]

with open("demo.csv","r") as x:
            reader= csv.DictReader(x)
            rows = list(reader)
            index = 0
            


            if (reader.fieldnames) != ['number', 'name', 'password', 'balance']:
                with open('demo.csv', mode='a') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()

class Account:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
        self.balance = input("Enter deposit amount : ")
    
    def save(self):
        number = ""
        for i in range(6):
            x = random.randint(1,9)
            number += str(x)
        fieldnames = ['number', 'name', 'password', "balance"]
        data = {"number": number, "name": self.name, "password": self.password, "balance": self.balance}
        print("\n")
        print("your account number is ({})".format(number))
        
        with open('demo.csv', mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(data)


class Bank:
    def __init__(self,name):
        self.name = name
    def update_csv(self, file_path, row_index, column_name, new_value):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        rows[row_index][column_name] = new_value

        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)


    def deposit(self, update_csv, account_no,amount):
        with open("demo.csv","r") as deposit:
            reader= csv.DictReader(deposit)
            rows = list(reader)
            index = 0

            for i in rows:
                if i["number"] == str(account_no):
                    new_balance = int(i["balance"]) + int(amount)
                    update_csv("demo.csv", index, "balance", new_balance)
                    print("Money deposit Successfully")

                index += 1


    def withdraw(self, update_csv, account_no,amount):
        with open("demo.csv","r") as withdraw:
            reader= csv.DictReader(withdraw)
            rows = list(reader)
            index = 0

            for i in rows:
                if i["number"] == str(account_no):
                    if int(i["balance"]) >= int(amount):
                        new_balance = int(i["balance"]) - int(amount)
                        update_csv("demo.csv", index, "balance", new_balance)
                        print("Money withdrawed Successfully")

                    else:
                        print("NO suffecint balance")
                index += 1


    def transfer(self, update_csv, account_no, reciver, amount):
        with open("demo.csv","r") as withdrow:
            reader= csv.DictReader(withdrow)
            rows = list(reader)
            index = 0

            for i in rows:
                if account_no == reciver:
                    print("BRUH!!!")
                else:    
                    if i["number"] == str(account_no):
                        if int(i["balance"]) >= int(amount):
                            new_balance = int(i["balance"]) - int(amount)
                            update_csv("demo.csv", index, "balance", new_balance)
                            print("Money transfered Successfully")

                        else:
                            print("NO suffecint balance")

                    if i["number"] == str(reciver):
                        new_balance = int(i["balance"]) + int(amount)
                        update_csv("demo.csv", index, "balance", new_balance)

                    index += 1    

bank = Bank("SWAT BANK")


def main():
    while True:
        print("\n===== Bank Signup & Login System =====")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create = Account()
            create.save()
        
        elif choice == "2":
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            
            with open("demo.csv","r") as withdrow:
                reader = csv.DictReader(withdrow)
                rows = list(reader)
                index = 0
                for i in rows:
                    if i["number"] == str(account_number):
                        if i["password"] == password:
                            print("")
                            print("Welcome {}".format(i["name"]))
                            print("Your balance is: {}".format(i["balance"]))
                            print("===== Bank Operations =====")
                            print("1. Deposit Money")
                            print("2. Withdraw Money")
                            print("3. Transfer Money")
                            print("4. Logout")
                            operation = input("Enter your operation: ")

                            if operation == "1":
                                amount = input("Please enter the amount you would like to deposit: ")
                                bank.deposit(bank.update_csv, account_number, amount)

                            elif operation == "2":
                                amount = input("Please enter the amount you would like to withdraw: ")
                                bank.withdraw(bank.update_csv, account_number, amount)

                            elif operation == "3":
                                amount = input("Please enter the amount you would like to transfer: ")
                                reciver = input("Please enter the account number of the reciver: ")
                                bank.transfer(bank.update_csv, account_number, reciver, amount)
                                                      
                            elif operation == "4":
                                print("Logging out...")
                                break
                            
                            else:
                                print("Invalid operation!")
                        else:
                            print("Invalid number or password Try again")
                    index += 1  

        elif choice == "3":
            print("exiting the program...")
            break

        else:
            print("Invalid option! Please try again")

if __name__ == "__main__":
    main()