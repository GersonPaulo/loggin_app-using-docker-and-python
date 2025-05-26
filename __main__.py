from cadstro import  Cadastro
import sys
new_user = Cadastro().registro_user()

class App:
    def __init__(self):
        self.new_user = new_user

    def create_new_user(self):
        insert = self.new_user


def display_menu():
    """Display the interactive menu."""
    print("\n=== App Menu ===")
    print("1. Register a new user")
    print("2. create")
    print("3. create")
    print("0. Exit\n")

    return input("Select an option: ")

def main():
    manager = App()
    while True:
        choice = display_menu()

        try:
            if choice == '1':
                manager.new_user()
                print("New User Created successfully!")
            elif choice == '0':
                print("Exiting...")
                sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()