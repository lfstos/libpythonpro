from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fernando', email="luiz-fernando@outlook.com")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Fernando', email="luiz-fernando@outlook.com"),
        Usuario(nome='Manon', email="santos.manon@hotmail.com")
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

