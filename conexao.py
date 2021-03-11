import mysql.connector

class Conexao:
    def __init__(self):
        self.host = "localhost"
        self.user = "andreone"
        self.password = "NaboBanco"

    
    def Conectar(self):
        global banco
        banco = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = "cad_livro"
        )
#cursor = banco.cursor()

#cursor.execute("CREATE TABLE Livros(idLivro INT NOT NULL AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(300), autor VARCHAR(300), genero VARCHAR(50), disciplina VARCHAR(200), editora VARCHAR(45))")



