class Login :
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




    def registro_user(self):
        u_mail = Login().add_mail()
        u_passe = Login().add_pase()
        self.users[u_mail] = self.u_passe
        return self.users
'''
    def verify_mail(self):
        verif_umail = Login().add_mail()
        while self.u_mail in self.users:
            print('E-mail já registrado')
            verif_umail = Login().add_mail()
        if self.u_mail not in self.users:
            self.users()[v]
            return False 
'''




a = Login().registro_user()
print(a)










