#Add an accomodation to the accomodation file
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

def readAccomodations(filename:str):
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        print(f'ID: {line.split(';')[0]}\nLocal: {line.split(';')[1]}\nTipology: {line.split(';')[2]}\nType: {line.split(';')[3]}\nPrice: {line.split(';')[4]}')
    return None

def readAccomodation(filename:str)-> None:
    id = input('Insert accomodation ID -> ')
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        if id in line.split(';')[3]:
            line = line.split(';')
            print(line[0]+line[1]+line[2]+line[3]+line[4])
        else:
            pass
    file.close()
    return None

def updateclient(filename:str):
    print(category)
    file = open(filename,'r')
    lines = file.readlines()
    file.close()
    with open(filename,'w') as file:
        for line in lines:
            if not idcard in line:
                file.write(line)
            else:
                a = line.split(';')
                print(a)
                add = ''
                if category.lower() == 'name':
                    a[0] = new
                elif category.lower() == 'age':
                    a[1] = new
                elif category.lower() == 'address':
                    a[2] = new
                elif category.lower() == 'idcard':
                    a[3] = new
                for element in a:
                    add += element
                file.write(add)
    return None

def removeclient(filename:str):
    idCard = input('ID Card -> ')
    file = open(filename, 'r')
    lines = file.readlines()
    lst = []
    for line in lines:
        if not idCard in line:
            lst.append(line)
    file.close
    with open(filename,'w') as file:
        for line in lst:
            file.write(line)
    return file
        

def checkclient():
    return None

def updateclient():
    return None