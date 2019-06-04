class Usuario():
    def __init__(self, nome, email, pais_origem, password):
        self.__nome = nome
        self.__email = email
        self.__pais_origem = pais_origem
        self.__password = password

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def pais_origem(self):
        return self.__pais_origem

    @pais_origem.setter
    def pais_origem(self, pais_origem):
        self.__pais_origem = pais_origem

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password