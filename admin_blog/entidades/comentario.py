class Comentario():
    def __init__(self, conteudo, post):
        self.__conteudo = conteudo
        self.__post = post

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self.__conteudo = conteudo

    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, post):
        self.__post = post