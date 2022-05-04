# pip install requests
# pip install python-firebase
# pip install git+https://github.com/ozgur/python-firebase

import email_scrape
from firebase import firebase

p = 0


firebase = firebase.FirebaseApplication(
    "https://hackathon-email-scraper-default-rtdb.firebaseio.com/", None
)


def scrape():
    email_scrape.Scraper()
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    print("~~~~~~~~~~~~~~ ")
    for y in email_scrape.mails:
        global newTeacherName
        global oldName
        global p
        oldName = y.lower()
        teacherName = oldName.replace("@mahoningctc.com", "")
        newTeacherName = teacherName.replace(".", " ")
        print(f"Teachers Email: {oldName}")
        print(f"Teachers name: {newTeacherName}")
        p += 1
        print(p)
        Create()


def Create():
    print(p)

    if p == 0:
        name = input("Insert name here: ")
        email = input("Insert email here: ")
    elif p >= 1:
        name = newTeacherName
        email = oldName
    else:
        print("null")

    print(f"Name: {name}")
    print(f"Email: {email}")

    newName = name.lower()

    data = {"name": newName, "email": email}
    result = firebase.post(f"/Zombie/Information/{newName}", data)
    x = result.get("name")


def Read():
    userName = input("Input name you would like to read: ")
    newName = userName.lower()

    result = firebase.get(f"/Zombie/Information/{newName}", "")

    # x = result.get('Name')
    # print(x)
    for i in result:
        print(i)
    print(result)


def Update():
    userName = input("Input name you would like to update: ")
    userInput = input("Input the subject you would like to change (Email, Name): ")
    userInput2 = input("Input what you would like to change it to: ")

    newName = userName.lower()
    newUserInput = userInput.lower()
    newUserInput2 = userInput2.lower()

    try:
        result = firebase.get(f"/Zombie/Information/{newName}", "")
        for x in result:
            print(x)
    except:
        print("Name not avaliable, please retry")
        Update()
    # x= result.get('name')
    # print(x)

    if newUserInput == "name" or newUserInput == "email":
        result = firebase.put(
            f"/Zombie/Information/{newName}/{x}", newUserInput, newUserInput2
        )
    else:
        print("Please type either Name or Email")
        Update()

    print("Updated")


def Delete():
    userName = input("Input name you would like to delete: ")
    newName = userName.lower()

    firebase.delete(f"Zombie/Information/{newName}", "")
    print("Deleted")


def option():
    i = input("Input C R U D: ")
    if i == "N":
        scrape()
    if i == "C":
        Create()
    if i == "R":
        Read()
    if i == "U":
        Update()
    if i == "D":
        Delete()
    # match i:
    #     case "C":
    #         Create()
    #     case "R":
    #         Read()
    #     case "U":
    #         Update()
    #     case "D":
    #         Delete()
    #     case "N":
    #         scrape()


option()
