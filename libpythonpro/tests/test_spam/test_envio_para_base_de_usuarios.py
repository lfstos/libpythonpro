import pytest
from libpythonpro.spam.modelos import Usuario

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam

@pytest.mark.parametrize(
    'usuarios', [
        [
            Usuario(nome='Fernando', email="luiz-fernando@outlook.com"),
            Usuario(nome='Manon', email="santos.manon@hotmail.com")
        ],
        [
            Usuario(nome='Fernando', email="luiz-fernando@outlook.com"),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luiz-fernando@outlook.com',
        'Curso Dev Pro',
        'Confira os módulos Fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados