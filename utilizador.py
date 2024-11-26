def createUser(filename: str) -> None:
    id = int(input("Insert ID: "))
    login = input("Insert login: ")
    password = input("Insert password: ")
    file = open(filename, 'a', encoding='utf-8')
    file.write(str(id) + ';' + login + ';' + password + '\n')
    file.close()
    return None

# Read a client from the client file
def readUser(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        if idcard in line.split(';')[0]:
            print(line.split(';')[0],line.split(';')[1],line.split(';')[2])
    file.close()
    return None

# Update a specific client in the client file
def updateUser(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if idcard in line.split(';')[0]:
            newlogin = input("Insert login: ")
            newpassword = input("Insert password: ")
            file.write(idcard + ';' + newlogin + ';' + newpassword + '\n')
        else:
            file.write(line)
    file.close()
    return None

# Delete a specific client in the client file
def deleteUser(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if not idcard in line.split(';')[0]:
            file.write(line)
    file.close()
    return None