from tabulate import tabulate
import pandas as pd

# Add a client to the client file
def createClient(filename: str) -> None:
    name = get_input("Insert Name: ")
    age = int(get_input("Insert Age: "))
    address = get_input("Insert Address: ")
    idCard = int(get_input("Insert IDCARD: "))
    file = open(filename, 'a', encoding='utf-8')
    file.write(name +';' + str(age) + ';' + address + ';' + str(idCard) + '\n')
    file.close()
    return None

# Read a client from the client file
def readClient(filename: str) -> None:
    idcard = get_input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    found = False
    for line in lines:
        if idcard in line.split(';')[3]:
            found = True
            client_data = line.strip().split(';')
            print(client_data[0], client_data[1], client_data[2], client_data[3])
            df = pd.DataFrame([client_data[:4]], columns=['Nome', 'Sobrenome', 'Idade', 'IDCARD'])
            print("\n=== Client ===")
            print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
            break
    if not found:
        print("Cliente não encontrado.")
    file.close()
    return None

# Update a specific client in the client file
def updateClient(filename: str) -> None:
    idcard = get_input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    updated = False
    for line in lines:
        if idcard in line.split(';')[3]:
            if not updated:
                newname = input("Insert Name: ")
                newage = int(input("Insert Age: "))
                newaddress = input("Insert Address: ")
                file.write(f"{newname};{newage};{newaddress};{idcard}\n")
                updated = True
        else:
            file.write(line)
    file.close()
    if not updated:
        print("Cliente não encontrado.")
    else:
        print("Cliente atualizado com sucesso.")
    return None

# Delete a specific client in the client file
def deleteClient(filename: str) -> None:
    idcard = get_input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if not idcard in line.split(';')[3]:
            file.write(line)
    file.close()
    return None

def ClientsTable() -> None:
    data = pd.read_csv('customers.csv', delimiter=';', dtype=str)
    print("\n=== List of Clients ===")
    print(tabulate(data, headers='keys', tablefmt="fancy_grid", showindex=False))

    return None

def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Nao digitou nada!")