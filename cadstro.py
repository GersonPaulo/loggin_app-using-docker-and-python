class Cadastro :
    def __init__(self):
        self.users = dict()
        self.u_mail = str()
        self.u_passe = str()

    #pede o email ao para o registro e verifica se o mail é valido
    def add_mail(self):
        temp_var = str(input('insira o seu email:>'))
        while "@" not in temp_var:
            print('E-mail invalido')
            temp_var = input('insira o seu email:>')
        if "@" in temp_var:
            self.u_mail = temp_var
            return  self.u_mail

    #pede a passe ao user e verificaa tem no min 8 caracteres
    def add_pase(self):
        temp_var = str(input('insira o sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            print('password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >= 8:
            self.u_passe = temp_var
            return self.u_passe


    def verify_mail_in_users(self):
        temp_u_mail = Cadastro().add_mail()
        while temp_u_mail in self.users:
            print('Mail já registado')
            temp_u_mail = Cadastro().add_mail()
        if temp_u_mail not in self.users:
            self.u_mail = temp_u_mail
            return self.u_mail

    def registro_user(self):
        u_mail = Cadastro().verify_mail_in_users()
        u_passe = Cadastro().add_pase()
        self.users[u_mail] = u_passe
        return self.users




a = Cadastro().registro_user()
print(a)










