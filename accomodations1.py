# Add an accomodation to the accomodation file
def createAccomodation(filename: str) -> None:
    id = int(input("Insert ID: "))
    local = input("Insert Local: ")
    tipology = input("Insert tipology: ")
    type = input("Insert type: ")
    price = float(input("Insert price: "))
    file = open(filename, 'a', encoding='utf-8')
    file.write(str(id) +';' + local + ';' + tipology + ';' + type + ';' + str(price) + '\n')
    file.close()
    return None

# Read a client from the client file
def readClient(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        if idcard in line.split(';')[3]:
            print(line.split(';')[0],line.split(';')[1],line.split(';')[2],line.split(';')[3])
    file.close()
    return None

# Update a specific client in the client file
def updateClient(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if idcard in line.split(';')[3]:
            newname = input("Insert Name: ")
            newage = int(input("Insert Age: "))
            newaddress = input("Insert Address: ")
            file.write(newname + ';' + str(newage) + ';' + newaddress + ';' + str(idcard) + '\n')
        file.write(line)
    file.close()
    return None

# Delete a specific client in the client file
def deleteClient(filename: str) -> None:
    idcard = input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if not idcard in line.split(';')[3]:
            file.write(line)
    file.close()
    return None