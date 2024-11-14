import manageaccomodations
import customers as managecustomers


def menu_principal():
    while True:
      try:
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
        opcao = int(input('Escolha uma opção: '))

        if 1 <= opcao <= 5:
                match opcao:
                    case 1:
                        manageaccomodations.createAccomodations('accomodations.csv')
                    case 2:
                        managecustomers.addClient('customers.csv')
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

def submenu():
    while True:
      try:
        print(
            " \n-----------------------------"
            " \nMENU CLIENTS:                  "
            ' \n1. Show Clients                '
            " \n2. Remove Clients              "
            " \n3. Update Client               "
            " \n4. Return                      "
            " \n-----------------------------"
        )

        sub_opcao = int(input("Escolha uma opção: "))

        if 1 <= sub_opcao <= 4:

            match sub_opcao:
                case 1:
                    managecustomers.ClientsTable()
                case 2:
                    managecustomers.removeClient('customers.csv')
                case 4:
                    return

        else:
            print("Option invalid")
      except KeyboardInterrupt:
          print('Desligou o programa')



def menuAccomodations():
    while True:
     try:
        print(
        "   \n-----------------------------"
            " \nMENU ACCOMODATIONS:       "
            ' \n1. Show Accomodations     '
            " \n2. Remove Accomodations   "
            " \n3. Update Accomodation    "
            " \n4. Return                 "
        "  \n -----------------------------"
              )
        opcaoAcc = int(input('Escolha uma opcao: '))

        if 1 <= opcaoAcc <= 4:
            match opcaoAcc:
                case 1:
                    manageaccomodations.AccomodationTable()
                case 2:
                    manageaccomodations.removeAccomodations('accomodations.csv')

                case 4:
                    return
        else:
            print("Option invalid")

     except KeyboardInterrupt:
         print('\nDesligou o programa!')

