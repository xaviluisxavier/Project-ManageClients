from tabulate import tabulate
import empty as pty
import pandas as pd

def createAccomodations(filename: str) -> None:

    idAcc = int(pty.get_input('Insert the idAcc: '))
    local = pty.get_input('Insert the local: ')
    tipology = pty.get_input('Insert the tipology: ')
    type = pty.get_input('Insert the type: ')
    price = int(pty.get_input('Insert the price: '))
    file = open(filename, 'a')
    file.write(str(idAcc) + ';' + local + ';' + tipology + ';' + type + ';' + str(price) + '\n')
    file.close()
    return None


def removeAccomodations(filename: str) -> None:
    idAcc = (pty.get_input('Insert IDACC: '))
    file = open('accomodations.csv', 'r', encoding='utf-8')
    text = file.read().split('\n')
    lst = []
    for line in text:
        lst.append(line.split(';'))
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for i in range(len(lst) - 1):
        if not idAcc == lst[i][0]:
            aux = ''
            for j in lst[i]:
                aux += str(j) + ';'

            file.write(aux[:-1] + '\n')
    file.close()

    return None


def updateAccomodations(filename: str) -> None:
    return None


def AccomodationTable() -> None:

    data = pd.read_csv('accomodations.csv', delimiter=';', dtype=str)
    print("\n=== List of Accomodations ===")
    print(tabulate(data, headers='keys', tablefmt="fancy_grid"))

    return None