from TesteOO import teste
from TesteOO import conexao


def Tela():
  opcao = 0
  while opcao != 5:

    print(''' [1] Cadastrar livro
    [2] Listar Livros
    [3] Excluir Livro
    [4] Alterar informações
    ''')
    opcao = int(input('O que deseja fazer? '))

    if opcao == 1:
      Cadastrar()
  
    if opcao == 2:
      Listar()
  
    if opcao == 3:
      Excluir()
    
    if opcao == 4:
      Update()

    

def Cadastrar():

  num_Lote = input('Qual é o Lote? ')
  empresa = input('Qual a empresa? ')
  autor = input('Qual o nome do autor? ')
  titulo = input('Qual o nome do titulo? ')
  genero = input('Qual o genero? ')
  disciplina = input('Qual a disciplina? ')
  editora = input('Qual o nome da Editora? ')
  
  livro1 = teste.Livro(num_Lote, empresa, autor, titulo, genero, disciplina, editora)
  livro1.CadastrarLivro()

#SELECT `idLivro` FROM `livros` WHERE( `titulo` = '%s');
#DELETE FROM `cad_livro`.`livros` WHERE (`idLivro` = 'idLivro');

def Update():
  #string '{}' para passar string
  #Passando o valor top
  cursor = conexao.banco.cursor()
  livroUP = input('Qual é o livro que você quer alterar? ')
  campo = input('O que você quer alterar? ')
  valor = input('Digite o novo {} '.format(campo))
  print(livroUP)

  comando_idLivro = "UPDATE livros SET {} = '{}' WHERE titulo ='{}';".format(campo,valor, livroUP)
  cursor.execute(comando_idLivro)
  conexao.banco.commit()

def Excluir():
  cursor = conexao.banco.cursor()
  livroDel = input('Qual é o livro que você quer excluir? ')
  print(livroDel)
  comando_idLivro = "SELECT idLivro FROM livros WHERE titulo = '{}';".format(livroDel)
  cursor.execute(comando_idLivro)
  for (idLivro) in cursor:
    print(idLivro)
    comando_SQL = "DELETE FROM `cad_livro`.`livros` WHERE (`idLivro` = '{:d}' );".format(idLivro[0])
    cursor.execute(comando_SQL)
    conexao.banco.commit()


 
  
  

def Listar():
  teste.ListarLivros()

Tela()