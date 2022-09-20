from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario():
    # Obtendo a conexão com o banco de dados. Gerencia a autenticação login e senha.
    conexao = Conexao()
    # Gerando sessões a partir da conexao obtida acima.
    # É utilizado efetivamente realizar as alterações como salvamento, busca e etc.
    sessao = conexao.gerar_sessao()
    # Criando um modelo simples Usuario, apenas com o nome
    usuario = Usuario(nome='Fernando')
    # Agora utilizo a sessão para salvar o usuário no banco
    sessao.salvar(usuario)
    # Cetificando que o usuário foi salvo. Toda vez que um usuário é salvo, ele recebe um
    # ID gerado automaticamente que se não definirmos nada, então será um int,
    # e vamos nos certificar que existe um ID e que é uma instancia de int.
    assert isinstance(usuario.id, int)
    # Após o teste finalizar, precisamos tomar alguns cuidados:
    # Desfazendo todas as alterações que foram feitas no momento do teste
    sessao.roll_back()
    # Fechando a sessão para liberar recursos
    sessao.fechar()
    # Após terminar de interagir com o banco, precisamos fechar a conexão
    conexao.fechar()

def test_listar_usuarios():
    # Obtendo a conexão com o banco de dados. Gerencia a autenticação login e senha.
    conexao = Conexao()
    # Gerando sessões a partir da conexao obtida acima.
    # É utilizado efetivamente realizar as alterações como salvamento, busca e etc.
    sessao = conexao.gerar_sessao()
    # Criando um modelo simples Usuario, apenas com o nome
    usuarios = [Usuario(nome='Fernando'), Usuario(nome='Manon')]
    # Agora utilizo a sessão para salvar o usuário no banco
    for usuario in usuarios:
        sessao.salvar(usuario)
    # Cetificando que o usuário foi salvo. Toda vez que um usuário é salvo, ele recebe um
    # ID gerado automaticamente que se não definirmos nada, então será um int,
    # e vamos nos certificar que existe um ID e que é uma instancia de int.
    assert usuarios == sessao.listar()
    # Após o teste finalizar, precisamos tomar alguns cuidados:
    # Desfazendo todas as alterações que foram feitas no momento do teste
    sessao.roll_back()
    # Fechando a sessão para liberar recursos
    sessao.fechar()
    # Após terminar de interagir com o banco, precisamos fechar a conexão
    conexao.fechar()