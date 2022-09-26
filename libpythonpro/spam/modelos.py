class Usuario:
    contador = 0
    def __init__(self, nome, email):
        # Adicinando o nome que recebemos como atributo na variável nome
        self.nome = nome
        self.email=email
        self.id = None
