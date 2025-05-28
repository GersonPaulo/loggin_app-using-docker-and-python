from databasemanager import DatabaseManager

db_manager = DatabaseManager()
class Cadastro :
    def __init__(self):
        self.u_mail = str()
        self.u_passe = str()
        self.users = dict()

    #pede o email ao para o registro e verifica se o mail é valido
    def add_mail(self):
        all_data = DatabaseManager().show_all_data()
        db_email = [user['email'] for user in all_data]
        j = 0
        while True:
            temp_var = input('insira o email:>')
            k = (temp_var in db_email) or ('@' not in temp_var)

            if k == True:
                if  ('@' not in temp_var):
                    print('=== E-mail invalido! ===')

                if (temp_var in db_email):
                    print('=== E-mail existente! ===')
                print({temp_var})

            elif k == False:
                self.u_mail = temp_var
                break

        return self.u_mail

    #pede a passe ao user e verifica tem no min 8 caracteres
    def add_passe(self):
        temp_var = str(input('insira a sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            print('password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >7:
            self.u_passe = temp_var
            print('password valida!')
            return self.u_passe

    def registro_user(self):
        u_mail = str(self.add_mail())
        u_passe = str(self.add_passe())
        DatabaseManager().insert_into_table(u_mail, u_passe)

    def mostrar_emails(self):
        all_data = DatabaseManager().show_all_data()
        i = 0
        print(f'{"---" * 5}')
        for user in all_data:
            i+=1
            print(f'user {i} email: {user["email"]}')
        print(f'{"---"*5}')




    def mostrar_passe(self):
        temp_var = str(input('digite o seu email:>'))
        all_data = DatabaseManager().show_all_data()
        i=0
        for user in all_data:
            i+=1
            j = True
            if temp_var == user["email"]:
                print(f'user Existente --- email: {user["email"]} match {temp_var}\n***<<Show Credentials>>***')
                print(f'{"---"*5} \nemail:{user["email"]} \npassword:{user["password"]} \n{"---"*5}')
                break
            else:
                j = False

        if j == False:print(f'{".." * i} {temp_var}***<<No Credentials>>***')


    def mustrar_user_and_pass(self):
        all_data = DatabaseManager().show_all_data()

        i = 0
        if len(all_data) > 0:
            for user in all_data:
                i += 1
                print(f"user: {i} -----> user_id: {user['user_id']}, email: {user['email']}, password: {user['password']}")
            print(f'no total temos {len(all_data)} users na prataforma')
        elif all_data == False:
            print('user table empty')

    def look_user_mail(self):
        temp_var = str(input('digite o seu email:>'))
        all_data = DatabaseManager().show_all_data()
        i = 0
        j = True
        for user in all_data:
            i += 1
            if temp_var == user["email"]:
                print(f'user Existente --- email: {user["email"]} match {temp_var}\n***<<Show Credentials>>***')
                print(f'{"---" * 5} \nemail:{user["email"]} \npassword:{user["password"]} \n{"---" * 5}')
                break

