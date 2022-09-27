class EnviadorDeSpam:

    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, destinatario, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                destinatario,
                usuario.email,
                assunto,
                corpo
            )
