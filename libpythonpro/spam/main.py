class EnviadorDeSpam:
    def __init__(self, sessao, Enviador):
        self.sessao = sessao
        self.enviador = Enviador

    def enviar_emails(self, destinatario, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                destinatario,
                usuario.email,
                assunto,
                corpo
            )
