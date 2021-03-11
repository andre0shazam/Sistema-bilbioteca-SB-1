import mysql.connector


from TesteOO import conexao

import lote as lote

conectarBD = conexao.Conexao()

conectarBD.Conectar()


#criar tabela
#cursor.execute("CREATE TABLE Livros(idLivro INT NOT NULL AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(300), autor VARCHAR(300), genero VARCHAR(50), disciplina VARCHAR(200), editora VARCHAR(45))")

class Livro(lote.Lote):
  def __init__(self,num_Lote, empresa, autor, titulo, genero, disciplina, editora):
    super().__init__(num_Lote,empresa)
    self.autor = autor
    self.titulo = titulo
    self.genero = genero
    self.disciplina = disciplina
    self.editora = editora
     
  def CadastrarLivro(self):
    #print(self.num_Lote,self.empresa, self.autor, self.titulo, self.editora) <<-- teste
    
    cursor = conexao.banco.cursor()
    comando_SQL = "INSERT INTO livros(num_Lote, empresa, titulo, autor, genero, disciplina, editora) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    dados = (self.num_Lote, self.empresa, self.titulo, self.autor, self.genero, self.disciplina, self.editora)
    cursor.execute(comando_SQL,dados)
    conexao.banco.commit()
    print(cursor)
    print ("livro cadastrado")
    

def ListarLivros():
  cursor = conexao.banco.cursor()
  comando_SQL = "SELECT * FROM cad_livro.livros"
  cursor.execute(comando_SQL)
  valores_lidos = cursor.fetchall()

  print('Listar livros')
  print(valores_lidos)
  
def ExcluirLivros(livroDel):
  
  cursor = conexao.banco.cursor()
  comando_SQL = "DELETE FROM `cad_livro`.`livros` WHERE (`titulo` = '%s');"
  cursor.execute(comando_SQL,livroDel)
  conexao.banco.commit()
  print(cursor)
  print(livroDel)
  print("excluir livros")


