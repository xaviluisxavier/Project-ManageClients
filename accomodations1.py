import customers as pty
from tabulate import tabulate
import pandas as pd

# Add an accomodation to the accomodation file
def createAccomodation(filename: str) -> None:
    id = int(pty.get_input("Insert ID: "))
    local = pty.get_input("Insert Local: ")
    tipology = pty.get_input("Insert tipology: ")
    type = pty.get_input("Insert type: ")
    price = float(pty.get_input("Insert price: "))
    file = open(filename, 'a', encoding='utf-8')
    file.write(str(id) +';' + local + ';' + tipology + ';' + type + ';' + str(price) + '\n')
    file.close()
    return None

# Read an accomodation from the accomodation file
def readAccomodation(filename: str) -> None:
    id = pty.get_input("Insert ID: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    found = False
    for line in lines:
        if id in line.split(';')[0]:
            found = True
            client_data = line.strip().split(';')
            print(client_data[0], client_data[1], client_data[2], client_data[3],client_data[4])
            df = pd.DataFrame([client_data[:5]], columns=['ID', 'Local', 'Tipology', 'Type', 'Price'])
            print("\n=== Client ===")
            print(tabulate(df, headers='keys', tablefmt="fancy_grid", showindex=False))
            break
    if not found:
        print("Cliente não encontrado.")
    file.close()
    return None

# Update a specific client in the client file
def updateAccomodation(filename: str) -> None:
    id = pty.get_input("Insert ID: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    updated = False
    for line in lines:
        if id in line.split(';')[0]:
            if not updated:
                local = input("Insert Local: ")
                tipology = input("Insert Tipology: ")
                type = input("Insert Type: ")
                price = int(input("Insert Price: "))
                file.write(f"{id};{local};{tipology};{type};{price}\n")
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
def deleteAccomodation(filename: str) -> None:
    id = pty.get_input("Insert ID: ")
    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for line in lines:
        if not id in line.split(';')[5]:
            file.write(line)
    file.close()
    return None

def listAccomodation(filename: str, length:int) -> None:
    lines = open(filename,'r').readlines()
    for line in lines:
        print(f'ID: {line.split(';')[0]}'
              f'\nLocal: {line.split(';')[1]}'
              f'\nTipology: {line.split(';')[2]}'
              f'\nType: {line.split(';')[3]}'
              f'\nPrice: {line.split(';')[4]}\n')
    return None

def listAny(filename: str, length:int) -> None:


    return None

def AccomodationTable() -> None:
        data = pd.read_csv('accomodations.csv', delimiter=';', dtype=str)
        print("\n=== List of Accomodations ===")
        print(tabulate(data, headers='keys', tablefmt="fancy_grid", showindex=False))

        return None