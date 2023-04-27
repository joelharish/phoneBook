phoneBook = {}


def getInputs():
    print("Select operation")
    print("===========================\n")
    print("""
        1. Add contact
        2. Edit contact
        3. Delete contact
        4. Search contact
        5. List contact
        6. Exit
        """)

    userInput = int(input("Enter your operation : "))

    if userInput == 1:
        insertData()
    elif userInput == 2:
        editData()
    elif userInput == 3:
        deleteData()
    elif userInput == 4:
        searchData()
    elif userInput == 5:
        listData()
    elif userInput == 6:
        exit()
    else:
        print("Invalid operation")


def insertData():
    while True:
        name = input("Enter the name : ")
        number = input("Enter the number : ")

        phoneBook[name] = number

        if phoneBook.items() == "":
            print("===============\n")
            print("Phone book empty\n")
            print("===============\n")
            insertData()
        else:
            print("===============\n")
            print("Contact added successfully\n")
            print("===============\n")
            getInputs()


def deleteData():
    name = input("Enter the name : ")

    if name in phoneBook:
        del phoneBook[name]
        print("===============\n")
        print(f"{name} deleted successfully\n")
        print("===============\n")
        getInputs()

    elif name not in phoneBook:
        print("===============\n")
        print(f"{name} not found\n")
        print("===============\n")
        while True:
            op = input("Are you continue this operation(Y/N) : ")
            if op == 'Y' or op == 'y':
                deleteData()
                break
            elif op == 'N' or op == 'n':
                getInputs()
                break
            else:
                print("Invalid selection")


def editData():
    name = input("Enter the name : ")

    if name in phoneBook.keys():
        newNumber = input("Enter the new number : ")
        phoneBook[name] = newNumber
        print("===============\n")
        print("Contact number changed successfully\n")
        print("===============\n")
    else:
        print("===============\n")
        print(f"{name} not found\n")
        print("===============\n")
    getInputs()


def searchData():
    searchRes = input("Enter the name your want search : ")

    if searchRes in phoneBook.keys():
        for i in phoneBook:
            if searchRes == i:
                print("===============\n")
                print(f"{i} :--> {phoneBook[i]}\n")
                print("===============\n")
        getInputs()
    else:
        print("===============\n")
        print(f"{searchRes} not in this phone book\n")
        print("===============\n")
        getInputs()


def listData():
    if phoneBook != "":
        print("===============")
        count = len(phoneBook)
        print(f"You hane {count} contacts\n")
        for item in phoneBook.keys():
            print(f"{item} :--> {phoneBook[item]}\n")
        print("===============\n")
        getInputs()


def main():
    getInputs()


main()
