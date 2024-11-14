from tabulate import tabulate

import pandas as pd

def createAccomodations(filename: str) -> None:
    id = int(input('Insert the id: '))
    local = input('Insert the local: ')
    tipology = input('Insert the tipology: ')
    type = input('Insert the type: ')
    price = (float(input('Insert the price: ')))
    file = open(filename, 'a')
    file.write(str(id) + ';' + local + ';' + tipology + ';' + type + ';' + str(price) + '\n')
    file.close()
    return None

def removeAccomodations(filename: str) -> None:
    id = int(input('Insert ID: '))
    file = open('accomodations.csv', 'r', encoding='utf-8')
    text = file.read().split('\n')
    lst = []
    for line in text:
        lst.append(line.split(';'))
    file.close()
    file = open(filename, 'w', encoding='utf-8')
    for i in range(len(lst) - 1):
        if not id == lst[i][1]:
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