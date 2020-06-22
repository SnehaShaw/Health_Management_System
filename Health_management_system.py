#health management system
list=["harry","Rohan","hammad"]
import datetime
def getdate():
    return datetime.datetime.now()
def add():
    a = int(input("press 1 for harry\npress 2 for Rohan\npress 3 for hammad"))
    if a == 1:
        b = int(input("in which field you want to log about harry\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1 :
            m=input("enter your suggession")
            with open("harry_food_log","a") as f :
                f.write(str([str(getdate())]) + ":" +m+ "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("harry_exercise_log","a") as f :
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
    elif a==2:
        b = int(input("in which field you want to log about Rohan\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1:
            m = input("enter your suggession")
            with open("rohan_food_log", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("rohan_exercise_log", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
    else:
        b = int(input("in which field you want to log about hammad\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1:
            m = input("enter your suggession")
            with open("hammad_food_log", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
        else:
            m = input("enter your suggession")
            with open("hammad_exercise_log", "a") as f:
                f.write(str([str(getdate())]) + ":" + m + "\n")
                print("successfully added")
def retrieve():
    a = int(input("press 1 for harry\npress 2 for Rohan\npress 3 for hammad"))
    if a == 1:
        b = int(input("what do you want to retrieve about harry\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1:
            with open("harry_food_log") as f:
                content=f.read()
                print(content)
        else:
            with open("harry_exercise_log") as f:
                content=f.read()
                print(content)
    elif a==2:
        b = int(input("what do you want to retrieve about rohan\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1:
            with open("rohan_food_log") as f:
                content = f.read()
                print(content)
        else:
            with open("rohan_exercise_log") as f:
                content = f.read()
                print(content)
    else:
        b = int(input("what do you want to retrieve about harry\nenter 1 for food log\n enter 2 for exercise log"))
        if b == 1:
            with open("hammad_food_log") as f:
                content = f.read()
                print(content)
        else:
            with open("hammad_exercise_log") as f:
                content = f.read()
                print(content)
s=int(input("what do you want either log data or retrieve\nenter 1 for log\n enter 2 for retrive"))
if s==1:
    add()
else:
    retrieve()
