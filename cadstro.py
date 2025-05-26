class Cadastro :
    def __init__(self):
        self.u_mail = str()
        self.u_passe = str()
        self.users = dict()


    #pede o email ao para o registro e verifica se o mail é valido
    def add_mail(self):
        temp_var = str(input('insira o seu email:>'))

        while ("@" not in temp_var) or temp_var in self.users:
            print('E-mail invalido ou já foi registado')
            temp_var = input('insira o seu email:>')

        if (temp_var not in self.users) and ('@' in temp_var):
            self.u_mail = temp_var
            return self.u_mail

    #pede a passe ao user e verifica tem no min 8 caracteres
    def add_passe(self):
        temp_var = str(input('insira o sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            print('password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >7:
            self.u_passe = temp_var
            print('password valida!')
            return self.u_passe

    def registro_user(self):
        u_mail = str(self.add_mail())
        u_passe = self.add_passe()
        self.users[f'{u_mail}'] = u_passe
        #print(self.users)

    def mostrar_users(self):
        for user in self.users:
            print(f'email: {user}')

    def mostrar_passe(self):
        user = input('digite o seu email:>')
        if user in self.users:
            print(f'email: {user}, \n passe: {self.users[f'{user}']}')