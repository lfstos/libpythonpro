import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario



def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fernando')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Fernando'), Usuario(nome='Manon')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

