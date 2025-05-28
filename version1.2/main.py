from cadastro import Cadastro
import sys

class App:
    def __init__(self):
        self.cadastro = Cadastro()

    def create_new_user(self):
        self.cadastro.registro_user()

    def see_emails(self):
        self.cadastro.mostrar_emails()

    def see_recover_user(self):
        self.cadastro.mostrar_passe()

    def see_user_and_pass(self):
        self.cadastro.mustrar_user_and_pass()

    #def menu_format(self):

def display_menu():
    """Display the interactive menu."""

    print("\n=== App Menu ===")
    print("1. Register a new user")
    print("2. List all user emails")
    print("3. Recover a user using email")
    print("4. list all users_id, email and password ")

    print("0. Exit")
    print("======" * 4,"\n")
    return input("Select an option: ")



def main():
    manager = App()
    while True:
        choice = display_menu()
        try:
            if choice == '1':
                print("1. Register a new user")
                manager.create_new_user()
                print("=== New User Created successfully!===")
            elif choice == '2':
                print("2. List all user emails")
                manager.see_emails()
                print("=== emails listed successfully! ===")
            elif choice == '3':
                print("3. Recover user password")
                manager.see_recover_user()
                print("=== User password recovered successfully! ===")
            elif choice == '4':
                print("4. list all, users_id emails and password ")
                manager.see_user_and_pass()
                print("=== successfully! ===")
            elif choice == '0':
                print("Exiting...")
                sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()