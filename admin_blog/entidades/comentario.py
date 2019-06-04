class Comentario():
    def __init__(self, conteudo, post, usuario):
        self.__conteudo = conteudo
        self.__post = post
        self.__usuario = usuario

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

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario