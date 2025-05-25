class Login :

    def __init__(self):
        self.users = dict()
        self.u_mail = str()
        self.u_passe = str()


    def add_mail(self):
        temp_var = str(input('insira o seu email:>'))
        while "@" not in temp_var:
            print('E-mail invalido')
            temp_var = input('insira o seu email:>')
        if "@" in temp_var:
            self.u_mail = temp_var
            return  self.u_mail

    def add_pase(self):
        temp_var = str(input('insira o sua password min 8 digitos:>'))
        while (len(temp_var)) <= 7 :
            print('password invalida minimo 8 digitos')
            temp_var = str(input('digite password:>'))
        if len(temp_var) >= 8:
            self.u_passe = temp_var
            return self.u_passe

    def regitro(self):
        u_mail = Login().add_mail()
        u_passe = Login().add_pase()
        self.users[u_mail] = u_passe
        return self.users

a = Login().regitro()
print(a)










