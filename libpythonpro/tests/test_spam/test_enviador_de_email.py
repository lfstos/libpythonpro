import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['luiz-fernando@outlook.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'fernandosantosdev@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'fernando']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'fernandosantosdev@gmail.com',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
