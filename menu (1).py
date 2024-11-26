import accomodations as ma
import clientes as mc
import listar
import alugar
import utilizador as user

print('MENU')

print('1 - Gerir alojamentos locais')
print('2 - Gerir clientes')
print('3 - Listar alojamentos e clientes')
print('4 - Consultar um alojamento local')
print('5 - Alugar um alojamento local')
print('6 - Classificar a experiência num alojamento local')
print('7 - Gerar relatório de atividade')
print('8 - Sair')

while True:
    opcao1 = int(input('Escolha uma opção -> '))
    if 1 <= opcao1 <= 8:
        match opcao1:
            case 1: 
                print('1 - Create Accomodation')
                print('2 - Read Accomodations')
                print('3 - Check Accomodation')
                print('4 - Update Accomodation')
                opcao2 = int(input('Escolha uma opção -> '))
                if 1 <= opcao2 <= 4:
                    match opcao2:
                        case 1: ma.createAccomodation('accomodations.csv')
                        case 2: listar.listAny('accomodations.csv',5)
                        case 3: pass
                        case 4: pass
                        case _: pass
            case 2:
                print('1 - Adicionar Cliente')
                print('2 - Remover Cliente')
                print('3 - Consultar Clintes')
                print('4 - Alteração de informação de um cliente')
                opcao2 = int(input('Escolha uma opção -> '))
                if 1 <= opcao2 <= 4:
                    match opcao2:
                        case 1: mc.createClient()
                        case 2: mc.deleteClient('customers.csv')
                        case 3: mc.readClients('customers.csv')
                        case 4: 
                            idcard = input('Insert ID Card -> ')
                            category = input('Choose a category: name|age|address|idcard ')
                            new = input('Insert what you want to change -> ')
                            mc.updateclient('customers.csv',idcard,category,new)
                        case _: pass

            case 3: 
                print('1 - Listar Clientes')
                print('2 - Listar Acomodações')
                opcao2 = int(input('Escolha uma opção -> '))
                if 1 <= opcao2 <= 2:
                    match opcao2:
                        case 1: listar.listAny('customers.csv',4)
                        case 2: listar.listAny('accomodations.csv',5)
                        case _: pass

            case 4: print('Opção 8')
            case 5: 
                print('1 - Create Book')
                print('2 - Read Book')
                print('3 - Update Book')
                print('4 - Delete Book')
                opcao2 = int(input('Escolha uma opção -> '))
                if 1 <= opcao2 <= 4:
                    match opcao2:
                        case 1: 
                            alugar.createBook()
                        case 2: user.updateUser('utilizadores.csv')
                        case 3: user.deleteUser('utilizadores.csv')
                        case 4: 
                            idClient = input('Insert ID -> ')
                            print(mc.getClient('customers.csv',idClient))
                        case _: pass
            case 6: print('Opção 8')
            case 7: print('Opção 8')
            case 8:
                break
    else:
        break
