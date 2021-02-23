import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetentes', ['luiz-fernando@outlook.com', 'teste@teste.com.br'])
def test_remetente(remetentes):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetentes,
        'ana@foobar.com.br',
        'Cursos Python Pro',
        'Primeira aula Guido Von Rossum aberta'

    )
    assert remetentes in resultado


@pytest.mark.parametrize('remetentes', ['', 'fernando'])
def test_rementente_invalido(remetentes):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
       enviador.enviar(
            remetentes,
            'ana@foobar.com.br',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
