from cadstro import  Cadastro
import sys

class App:
    def __init__(self):
        self.cadastro = Cadastro()


    def create_new_user(self):
        self.cadastro.registro_user()


    def see_users(self):
        self.cadastro.mostrar_users()

    def see_recover_user(self):
        self.cadastro.mostrar_passe()




def display_menu():
    """Display the interactive menu."""
    print("\n=== App Menu ===")
    print("1. Register a new user")
    print("2. List all registered users")
    print("3. Recover a user")
    print("0. Exit\n")
    return input("Select an option: ")

def main():
    manager = App()
    while True:
        choice = display_menu()
        try:
            if choice == '1':
                manager.create_new_user()
                print("New User Created successfully!")
            elif choice == '2':
                manager.see_users()
                print("Users listed successfully!")
            elif choice == '3':
                manager.see_recover_user()
            elif choice == '0':
                print("Exiting...")
                sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()