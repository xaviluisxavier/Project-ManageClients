#Print all clients from the client file
def listClients(filename:str) -> None:
    lines = open(filename,'r').readlines()
    for line in lines:
        print(f'Name: {line.split(';')[0]}\nAge: {line.split(';')[1]}\nAddress: {line.split(';')[2]}\nID Card: {line.split(';')[3]}\n')
    return None

#Print all accomodations from the accomodation file
def listAccomodations(filename:str) -> None:
    lines = open(filename,'r').readlines()
    for line in lines:
        print(f'ID: {line.split(';')[0]}\nLocal: {line.split(';')[1]}\nTipology: {line.split(';')[2]}\nType: {line.split(';')[3]}\nPrice: {line.split(';')[4]}')
    return None


def listAny(filename:str, length:int) -> None:
    lines = open(filename,'r').readlines()
    for line in lines:
        for i in range(length):
            print(f'{i}: {line.split(';')[i]}')
    return None
