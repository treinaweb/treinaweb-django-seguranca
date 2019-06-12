class Post():
    def __init__(self, titulo, descricao, conteudo, categoria, capa):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__conteudo = conteudo
        self.__categoria = categoria
        self.__capa = capa

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self.__conteudo = conteudo

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def capa(self):
        return self.__capa

    @capa.setter
    def capa(self, capa):
        self.__capa = capa