import os
import json
new_user = True
right_password = False
#to do
#autoremoving income and expenses
budget = 0

if not(os.path.exists("base.json")): #creating database if not present
    with open("base.json","w")as f:
        f.write("[\n]")
    
def getting_user_data_json_old_user():
    global expenses
    global income
    global budget
    expenses = base[user_id].get("expenses")
    income = base[user_id].get("income")
    budget = sum(income.values()) - sum(expenses.values())

def updating_database():
    global budget
    budget = sum(income.values()) - sum(expenses.values()) #getting budget 
    base[user_id].update({"budget":budget}) #updating base
    with open("base.json","w")as f: #updating file
        f.truncate(0)
        f.seek(0)
        json.dump(base,fp=f,indent=4)

def checking_username():
    global user_id
    for i in base:
        if i["username"] == username:
            checking_password()
            global new_user
            new_user = False
    if new_user == True:  #new user
        global expenses
        global income
        global budget
        print("create your password")
        password = input()
        expenses = {}
        income = {}
        budget = 0
        base.append({"username":username,
                     "password":password,
                     "budget":0,
                     "expenses":{},
                     "income":{}})
        user_id = len(base)-1
        updating_database()
        control_panel()

def checking_password():
    global user_id
    global password
    global right_password
    print("put your password")
    password = input()
    for i in base:
        if i["password"] == password:
            user_id = base.index(i)
            print("welcome back")
            right_password = True
            getting_user_data_json_old_user()
            control_panel()
    if right_password == False:
        print("wrong password")
        print("please try again")
        checking_password()

def control_panel():
    print(f"this is your budget {budget}")
    print(f"those are your expenses {expenses}")
    print(f"this is your income {income}")
    print("if you want to display this panel again write con")

def help():
    print("con displays control panel")
    print("add_exp adds expense ")
    print("add_inc adds income")
    print("quit quits")
    print("help displays help panel")

def add_exp():
    global expenses
    if len(expenses) > 10:
        del expenses[list(expenses.keys())[0]]
    print("name of expense")
    name = input()
    print("cost")
    cost = int(input())
    expenses.update({name:cost})
    base[user_id].get("expenses").update({name:cost})
    updating_database()

def add_inc():
    if len(income) > 10:
        del income[list(income.keys())[0]]
    print("name of the income")
    name = input()
    print("income size")
    size = int(input())
    income.update({name:size})
    base[user_id].get("income").update({name:size})
    updating_database()

print("put your username")
username = input()
with open("base.json","r")as f: #opening database in python
    base = json.loads(f.read())
    checking_username()

while True: #command line
    command = input(">")
    if command == "con":
        control_panel()
    elif command == "add_exp":
        add_exp()
    elif command == "add_inc":
        add_inc()
    elif command == "quit":
        break
    elif command == "help":
        help()
    else:
        print("wrong command")
