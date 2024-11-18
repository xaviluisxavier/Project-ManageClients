from tabulate import tabulate
import empty as pty
import pandas as pd

def createAccomodations(filename: str) -> None:

    idAcc = int(pty.get_input('Insert the idAcc: '))
    local = pty.get_input('Insert the local: ')
    tipology = pty.get_input('Insert the tipology: ')
    type = pty.get_input('Insert the type: ')
    price = float(pty.get_input('Insert the price: '))
    file = open(filename, 'a')
    file.write(str(idAcc) + ';' + local + ';' + tipology + ';' + type + ';' + f"{price:.2f}" + '\n')
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

    idAcc = pty.get_input('Insert IDACC to edit: ')
    file = open(filename, 'r', encoding='utf-8')
    text = file.read().split('\n')
    lst = []
    for line in text:
        lst.append(line.split(';'))
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for i in range(len(lst) - 1):
        if lst[i][0] == idAcc:

            new_local = pty.get_input("Enter new LOCAL: ")
            new_tipology = pty.get_input("Enter new TIPOLOGY: ")
            new_type = pty.get_input("Enter new TYPE: ")
            new_price = pty.get_input("Enter new PRICE: ")

            lst[i][1] = new_local
            lst[i][2] = new_tipology
            lst[i][3] = new_type
            lst[i][4] = new_price
        aux = ''
        for j in lst[i]:
            aux += str(j) + ';'
        file.write(aux[:-1] + '\n')
    else:
        print('ID nao é valido!')

        file.close()
        return None


def AccomodationTable() -> None:

    data = pd.read_csv('accomodations.csv', delimiter=';', dtype=str)
    print("\n=== List of Accomodations ===")
    print(tabulate(data, headers='keys', tablefmt="fancy_grid", showindex=False))

    return None

