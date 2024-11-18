import accomodations1 as acc
import customers as managecustomers


def menu_principal():
    while True:

        print(
        "\n-----------------------------"
        "\n MENU:                            "
        "\n1. Add Accomodations              "
        "\n2. Add Clients                    "
        "\n3. Manage Clients                 "
        "\n4. Manage Accomodations           "
        "\n5. Exit                           "
        "\n-----------------------------"
        )

        try:
            opcao = int(managecustomers.get_input('Escolha uma opção: '))


            if 1 <= opcao <= 5:
                match opcao:
                    case 1:
                        acc.createAccomodation('accomodations.csv')
                    case 2:
                        managecustomers.createClient('customers.csv')
                    case 3:
                        submenu()
                    case 4:
                        menuAccomodations()
                    case 5:
                        break
            else:
                print("Option invalid")
        except KeyboardInterrupt:
            print('\nDesligou o programa!')
            break


def submenu():
    while True:

        print(
            " \n-----------------------------"
            " \nMENU CLIENTS:                  "
            ' \n1. Show Clients                '
            " \n2. Remove Clients              "
            " \n3. Update Client    "
            " \n4. Read Client       "
            " \n5. Return                      "
            " \n-----------------------------"
        )
        try:
            sub_opcao = int(managecustomers.get_input("Escolha uma opção: "))


            if 1 <= sub_opcao <= 5:

                match sub_opcao:
                    case 1:
                        managecustomers.ClientsTable()
                    case 2:
                        managecustomers.deleteClient('customers.csv')
                    case 3:
                        managecustomers.updateClient('customers.csv')
                    case 4:
                        managecustomers.readClient('customers.csv')
                    case 5:
                        return

            else:
                print("Option invalid")
        except KeyboardInterrupt:
            print('\nDesligou o programa!')
            break



def menuAccomodations():
    while True:

        print(
        "   \n-----------------------------"
            " \nMENU ACCOMODATIONS:       "
            ' \n1. Show Accomodations     '
            " \n2. Remove Accomodations   "
            " \n3. Update Accomodation"
            " \n4. Read Accomodation    "
            " \n5. Return                 "
        "  \n -----------------------------"
        )
        try:

            opcaoAcc = int(managecustomers.get_input('Escolha uma opcao: '))



            if 1 <= opcaoAcc <= 5:
                match opcaoAcc:
                    case 1:
                        acc.AccomodationTable()
                    case 2:
                        acc.deleteAccomodation('accomodations.csv')
                    case 3:
                        acc.updateAccomodation('accomodations.csv')
                    case 4:
                        acc.readAccomodation('accomodations.csv')
                    case 5:
                        return
            else:
                print("Option invalid")

        except KeyboardInterrupt:
         print('\nDesligou o programa!')
         break