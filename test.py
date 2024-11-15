import manageaccomodations
import customers as managecustomers
import empty as pty
import os

USERS_FILE = "users.txt"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpass"
CIBERNAUTA_USERNAME = "ciber"
CIBERNAUTA_PASSWORD = "ciberpass"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_users():
    users = {
        ADMIN_USERNAME: {"password": ADMIN_PASSWORD, "type": "Admin"},
        CIBERNAUTA_USERNAME: {"password": CIBERNAUTA_PASSWORD, "type": "Cibernauta"}
    }
    if os.path.exists(USERS_FILE):
        file = open(USERS_FILE, "r")
        for line in file:
            username, password, user_type = line.strip().split(":")
            users[username] = {"password": password, "type": user_type}
        file.close()
    return users


def save_users(users):
    file = open(USERS_FILE, "w")
    for username, user_data in users.items():
        if username not in [ADMIN_USERNAME, CIBERNAUTA_USERNAME]:
            file.write("{}:{}:{}\n".format(username, user_data["password"], user_data["type"]))
    file.close()


def register(users):
    clear_screen()
    print("=== Registro de Novo Utilizador ===")
    username = input("Nome de utilizador: ")
    if username in users:
        print("Erro: Este nome de utilizador já existe!")
    else:
        password = input("Senha: ")
        users[username] = {"password": password, "type": "normal"}
        save_users(users)
        print("Utilizador {} registrado como utilizador normal!".format(username))



def login(users):
    clear_screen()
    print("=== Login ===")
    username = input("Nome de utilizador: ")
    password = input("Senha: ")
    if username in users and users[username]["password"] == password:
        print("Login bem-sucedido! Bem-vindo, {} {}.".format(users[username]["type"], username))
        return username
    else:
        print("Utilizador ou senha incorretos!")

        return None


def menu_principal(user_type):
    while True:
        clear_screen()
        print("\n-----------------------------")
        print("MENU:")
        if user_type == "Admin":
            print("1. Add Accomodations")
            print("2. Add Clients")
            print("3. Manage Clients")
            print("4. Manage Accomodations")
        elif user_type == "Cibernauta":
            print("1. List Accomodations")
            print("2. Update Accomodations")
        else:  # Utilizador normal
            print("1. Rent Accomodation")
            print("2. Rate Accomodation")
        print("5. Exit")
        print("-----------------------------")

        try:
            opcao = int(pty.get_input('Escolha uma opção: '))

            if user_type == "Admin":
                if 1 <= opcao <= 5:
                    match opcao:
                        case 1:
                            manageaccomodations.createAccomodations('accomodations.csv')
                        case 2:
                            managecustomers.addClient('customers.csv')
                        case 3:
                            submenu(user_type)
                        case 4:
                            menuAccomodations(user_type)
                        case 5:
                            break
                else:
                    print("Option invalid")
            elif user_type == "Cibernauta":
                if 1 <= opcao <= 5:
                    match opcao:
                        case 1:
                            manageaccomodations.AccomodationTable()
                        case 2:
                            manageaccomodations.updateAccomodations('accomodations.csv')
                        case 5:
                            break
                else:
                    print("Option invalid")
            else:  # Utilizador normal
                if 1 <= opcao <= 5:
                    match opcao:
                        case 1:
                            rent_accomodation()
                        case 2:
                            rate_accomodation()
                        case 5:
                            break
                else:
                    print("Option invalid")
        except KeyboardInterrupt:
            print('\nDesligou o programa!')
            break


def submenu(user_type):
    while True:
        clear_screen()
        print("\n-----------------------------")
        print("MENU CLIENTS:")
        print("1. Show Clients")
        print("2. Remove Clients")
        print("3. Update Client")
        print("4. Return")
        print("-----------------------------")

        try:
            sub_opcao = int(pty.get_input("Escolha uma opção: "))

            if 1 <= sub_opcao <= 4:
                match sub_opcao:
                    case 1:
                        managecustomers.ClientsTable()
                    case 2:
                        managecustomers.removeClient('customers.csv')
                    case 3:
                        managecustomers.updateClient('customers.csv')
                    case 4:
                        return
            else:
                print("Option invalid")
        except KeyboardInterrupt:
            print('\nDesligou o programa!')
            break


def menuAccomodations(user_type):
    while True:
        clear_screen()
        print("\n-----------------------------")
        print("MENU ACCOMODATIONS:")
        print("1. Show Accomodations")
        print("2. Remove Accomodations")
        print("3. Update Accomodation")
        print("4. Return")
        print("-----------------------------")

        try:
            opcaoAcc = int(pty.get_input('Escolha uma opcao: '))

            if 1 <= opcaoAcc <= 4:
                match opcaoAcc:
                    case 1:
                        manageaccomodations.AccomodationTable()
                    case 2:
                        manageaccomodations.removeAccomodations('accomodations.csv')
                    case 3:
                        manageaccomodations.updateAccomodations('accomodations.csv')
                    case 4:
                        return
            else:
                print("Option invalid")
        except KeyboardInterrupt:
            print('\nDesligou o programa!')
            break






def main_menu():
    users = load_users()
    while True:
        clear_screen()
        print("=== Sistema de Login ===")
        print("1. Login")
        print("2. Registrar (apenas para utilizadores normais)")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            logged_user = login(users)
            if logged_user:
                menu_principal(users[logged_user]["type"])
        elif choice == '2':
            register(users)
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")



