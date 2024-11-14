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
    idAcc = pty.get_input('Insert IDACC to edit: ')

    file = open(filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    file = open(filename, 'w', encoding='utf-8')

    for line in lines:
        fields = line.strip().split(';')
        if fields[0] == idAcc:

            new_local = pty.get_input("Enter new LOCAL: ")
            new_tipology = pty.get_input("Enter new TIPOLOGY: ")
            new_type = pty.get_input("Enter new TYPE: ")
            new_price = pty.get_input("Enter new PRICE: ")

            # Cria a nova linha
            new_line = f"{idAcc};{new_local};{new_tipology};{new_type};{new_price}\n"
            file.write(new_line)
        else:
            file.write(line)

    file.close()

    return None


def AccomodationTable() -> None:

    data = pd.read_csv('accomodations.csv', delimiter=';', dtype=str)
    print("\n=== List of Accomodations ===")
    print(tabulate(data, headers='keys', tablefmt="fancy_grid"))

    return None