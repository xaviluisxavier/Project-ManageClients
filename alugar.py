import clientes as cli
import datetime as dat

#Create a Book on the book file
def createBook() -> None:
    id = input('Insert the accomodation ID -> ')
    idClient = input('Insert the client ID -> ')
    if not cli.getClient('customers.csv',idClient) == '':
        year = int(input('Insert the year -> '))
        month = int(input('Insert the month -> '))
        day = int(input('Insert the day -> '))
        if dat.datetime.now() < dat.datetime(year,month,day):
            guests = int(input('Insert the max amount of guests -> '))
            file = open('book.csv','a')
            file.write(id + ';' + str(cli.getClient('customers.csv',idClient).split(';')) + ';' + str(dat.datetime.now()) + ';' + str(dat.datetime(year,month,day)) + ';' + str(guests) + '\n')
            file.close()
        else:
            print('The check-in date is greater than check-out.')
    else:
        print('Client does not exist.')
    return None

#Read a Book from the book file
def readBook(filename:str)-> None:
    id = input('Insert ID -> ')
    lines = open(filename,'r').readlines()
    for line in lines:
        if id in line.split(';')[0]:
            print(line.split(';')[0],line.split(';')[1],line.split(';')[2],line.split(';')[3])
        else:
            pass
    return None

#Update a specific characteristic from a Book in the book File
def updateBook(filename:str):
    id = input('Insert ID -> ')
    lines = open(filename,'r').readlines()
    with open(filename,'w') as file:
        for line in lines:
            if not id in line:
                file.write(line)
            else:
                newcheck_in = input('Insert check-in date -> ')
                newcheck_out = input('Insert check-out date -> ')
                newguests = int(input('Insert the max amount of guests -> '))
                file.write(id + ';' + newcheck_in + ';' + newcheck_out + ';' + str(newguests) + '\n')
    return None

#Removes a Book from the book File
def deleteBook(filename:str):
    id = input('Insert ID -> ')
    lines = open(filename, 'r').readlines()
    with open(filename,'w') as file:
        for line in lines:
            if not id in line.split(';')[0]:
                file.write(line)
    return file
