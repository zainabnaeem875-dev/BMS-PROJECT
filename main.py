
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("file is not exist")
    except Exception as err:
        print(f"the error has occured {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __AccountGenetrate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):
        info = {
            "name": input("tell your name:"),
            "age": int(input("tell your age:")),
            "email": input("tell your email:"),
            "pin": int(input("tell your 4 number pin:")),
            "accountNo": Bank.__AccountGenetrate(),
            "balance": 0,
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry You cannot create an Account")
        else:
            print("Account has been ceated Successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account Number:")
        pin = input("please tell your pin:")

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("sorry data not found")
        else:
            amount = int(input("how much want to deposit"))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much  you can deposit below 10000 and above 100")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("amount deposite successfully")

    def withdrawmoney(self):
            accnumber = input("please tell your account Number:")
            pin = input("please tell your pin:")
    
            userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
            if userdata == False:
                print("sorry data not found")
            else:
                amount = int(input("how much want to withdraw"))
                if userdata[0]['balance'] < amount:
                    print("sorry the amount is too much  you cannot withdraw")
                else:
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print("amount withdarw successfully")

    def showdetais(self):
        accnumber = input("please tell your account Number:")
        pin = input("please tell your pin:")
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("your information are \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("please tell your account Number:")
        pin = input("please tell your pin:")
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("user not found ")
        else:
            print("you cannot change age , balance and account number")
            print("fill the details for change or leave it empty if no change")
            newdata = {
                "name": input("tell your NewName"),
                "email": input("tell your New Email"),
                "pin": input("enter your New pin"),
            }


            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]["age"]
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                  userdata[0][i] = newdata[i]  
            Bank.__update()
            print("update details succesfully")

    def delete(self):
        accnumber = input("please tell your account Number:")
        pin = input("please tell your pin:")
        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("data not found")
        else:
            check = input("press y if you actually want to delet the accunt or press n")
            if check == 'n' or check == "N":
                print("pass")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account delete successfully")
                Bank.__update()



user = Bank()

print("press 1 for Create an Account")
print("press 2 for Deposit the money in the bank")
print("press 3 for Withdraw the money in the bank")
print("press 4 for Details")
print("press 5 for Updating the details")
print("press 6 for Delete the Account")

check = int(input("tell your Response"))

if check == 1:
    user.CreateAccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetais()
if check == 5:
    user.updatedetails()
if check == 6:
    user.delete()