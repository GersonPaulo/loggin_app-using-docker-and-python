
class Cadastro :

    def __init__(self):
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
            return 'add_mail', self.u_mail

    #pede a passe ao user e verificaa tem no min 8 caracteres
    def add_passe(self):
        print(111, self.u_mail)
        temp_var = str(input('insira o sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            print('password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >= 8:
            self.u_passe = temp_var
            return 'add passe', self.u_passe


    def verify_mail_in_users(self, users={}):
        temp_u_mail = self.add_mail()
        while temp_u_mail in users:
            print('Mail já registado')
            temp_u_mail = self.add_mail()
        if temp_u_mail not in users:
            self.u_mail = temp_u_mail
            #return 'verify',self.u_mail

    def registro_user(self, users={}):
        u_mail = self.verify_mail_in_users()
        u_passe = self.add_passe()
        users[u_mail] = u_passe
        return 'registro', users[u_mail]

    def mostrar_users(self):
        pass







a = Cadastro().registro_user()
#b = Cadastro().add_mail()

print(1, a)

print(1, b, a)










