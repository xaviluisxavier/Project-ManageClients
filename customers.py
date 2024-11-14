from tabulate import tabulate
import empty as pty
import pandas as pd


def addClient(filename: str) -> None:

        name = pty.get_input("Insert Name: ")
        age = int(pty.get_input("Insert Age: "))
        address = pty.get_input("Insert Address: ")
        idCard = int(pty.get_input("Insert IDCARD: "))
        file = open(filename, 'a', encoding='utf-8')
        file.write(name +';' + str(age) + ';' + address + ';' + str(idCard) + '\n')
        file.close()



def readClient() -> None:

    return None


def removeClient(filename: str) -> None:
    idcard = pty.get_input("Insert IDCARD: ")
    file = open(filename, 'r', encoding='utf-8')
    text = file.read().split('\n')
    lst = []
    for line in text:
        lst.append(line.split(';'))
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for i in range(len(lst) - 1):
        if not idcard == lst[i][3]:
            aux = ''
            for j in lst[i]:
                aux += str(j) + ';'

            file.write(aux[:-1] + '\n')  # Remove o último ';' antes de escrever
    file.close()
    return None


def updateClient() -> None:

    return None




def ClientsTable() -> None:
    data = pd.read_csv('customers.csv', delimiter=';', dtype=str)
    print("\n=== List of Clients ===")
    print(tabulate(data, headers='keys', tablefmt="fancy_grid"))

    return None


