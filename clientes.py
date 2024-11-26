#Create a Client on the Client File
def createClient():
    nome = input('Name -> ')
    age = int(input('Age -> '))
    address = input('Address -> ')
    idCard = input('Cartão de Cidadão -> ')
    file = open('customers.csv','a')
    file.write('\n' + nome + ';' + str(age) + ';' + address + ';' + idCard)
    file.close()
    return None

#Read a Client from the Client File
def readClient(filename:str, id:str = '')-> None:
    idCard = input('Insert IDCARD -> ')
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        if idCard in line.split(';')[3]:
            print(line.split(';')[0]+line.split(';')[1]+line.split(';')[2]+line.split(';')[3])
        else:
            pass
    file.close()
    return None

#Update a specific characteristic from a Client in the Client File
def updateclient(filename:str, idcard:str,category:str,new:str):
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

#Removes a Client from the Client File
def deleteClient(filename:str):
    idcard = input('Insert ID Card -> ')
    file = open(filename, 'r')
    lines = file.readlines()
    lst = []
    for line in lines:
        if not idcard in line:
            lst.append(line)
    file.close
    with open(filename,'w') as file:
        for line in lst:
            file.write(line)
    return file

def getClient(filename:str,idClient:str)-> str:
    file = open(filename,'r')
    lines = file.readlines()
    file.close()
    for line in lines:
        if idClient in line.split(';')[3]:
            return line
    return '' 










def readClients(filename:str):
    file = open(filename,'r')
    lines = file.readlines()
    lst = []
    for line in lines:
        lst = line.split(';')
        name = lst[0]
        age = lst[1]
        address = lst[2]
        idcard = lst[3]
        print(f'Name: {name}\nAge: {age}\nAddress: {address}\nID Card: {idcard}\n')
    return None



# O PROF FEZ ESTA PARTE
#def removeclient(filename:str):
#    idCard = input('ID Card -> ')
#    file = open(filename, 'r')
#    text = file.read().split('\n')
#    lst = []
#    for line in text:
#        lst.append(line.split(';')) 
#    file.close
#    
#    file = open(filename,'w',encoding='utf8')
#    for i in lst:
#        if not idCard == lst[i][3]:
#            aux = ''
#            for j in lst[i]:
#                aux = aux + lst[i][j] + ';'
#            file.write(aux + '\n')
#    return None
#
#def updateclient(filename:str, idcard:str,category:str,new:str):
#    print(category)
#    file = open(filename,'r')
#    lines = file.readlines()
#    lst = []
#    for line in lines:
#        if not idcard in line:
#            lst.append(line)
#        else:
#            a = line.split(';')
#            print(a)
#            add = ''
#            if category.lower() == 'name':
#                a[0] = new
#            elif category.lower() == 'age':
#                a[1] = new
#            elif category.lower() == 'address':
#                a[2] = new
#            elif category.lower() == 'idcard':
#                a[3] = new
#            for element in a:
#                add += element
#            lst.append(add)
#    print(lst)
#    file.close()
#    with open(filename,'w') as file:
#        for line in lst:
#            print(line)
#
#    return None
#
#def updateclient(filename:str, idcard:str,category:str,new:str):
#    print(category)
#    file = open(filename,'r')
#    lines = file.readlines()
#    file.close()
#    with open(filename,'w') as file:
#        for line in lines:
#            if not idcard in line:
#                file.write(line)
#            else:
#                a = line.split(';')
#                print(a)
#                add = ''
#                if category.lower() == 'name':
#                    a[0] = new
#                elif category.lower() == 'age':
#                    a[1] = new
#                elif category.lower() == 'address':
#                    a[2] = new
#                elif category.lower() == 'idcard':
#                    a[3] = new
#                for element in a:
#                    add += element
#                file.write(add)
#    return None
#
#def removeClient(filename:str,idCard:str):
#    file = open(filename, 'r')
#    lines = file.readlines()
#    lst = []
#    file.close
#    with open(filename,'w') as file:
#        for line in lines:
#            if not idCard in line:
#                file.write(line)
#    return file
