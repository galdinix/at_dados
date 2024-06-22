import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('bibliotecaOnline.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Autor (
    id_autor INTEGER PRIMARY KEY,
    nome_autor varchar(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria INTEGER PRIMARY KEY,
    nome_categoria varchar(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Editora (
    id_editora INTEGER PRIMARY KEY,
    nome_editora varchar(50) NOT NULL,
    pais_publicacao varchar(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro (
    id_livro INTEGER PRIMARY KEY,
    titulo varchar(50) NOT NULL,
    isbn varchar(15) UNIQUE NOT NULL,
    id_autor INTEGER,
    id_categoria INTEGER,
    id_editora INTEGER,
    FOREIGN KEY (id_autor) REFERENCES Autor (id_autor),
    FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria),
    FOREIGN KEY (id_editora) REFERENCES Editora (id_editora)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Biblioteca_online (
    id_biblioteca INTEGER PRIMARY KEY,
    id_autor INTEGER,
    id_categoria INTEGER,
    id_editora INTEGER,
    FOREIGN KEY (id_autor) REFERENCES Autor (id_autor),
    FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria),
    FOREIGN KEY (id_editora) REFERENCES Editora (id_editora)
)
''')

# Função para inserir dados iniciais no banco
def plot_bd():
    cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome_autor) VALUES (1, 'Fyodor Dostoyevsky')")
    cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome_autor) VALUES (2, 'George Orwell')")
    cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome_autor) VALUES (3, 'Franz Kafka')")
    cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome_autor) VALUES (4, 'Antoine de Saint-Exupéry')")

    cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome_categoria) VALUES (1, 'Ficção')")
    cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome_categoria) VALUES (2, 'Não Ficção')")
    cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome_categoria) VALUES (3, 'Romance')")

    cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome_editora, pais_publicacao) VALUES (1, 'Penguin Books', 'Rússia')")
    cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome_editora, pais_publicacao) VALUES (2, 'Penguin Books', 'Reino Unido')")
    cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome_editora, pais_publicacao) VALUES (3, 'Vintage Books', 'Áustria')")
    cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome_editora, pais_publicacao) VALUES (4, 'Vintage Books', 'França')")

    cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, isbn, id_autor, id_categoria, id_editora) VALUES (1, 'Crime e Castigo', '1234567890', 1, 1, 1)")
    cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, isbn, id_autor, id_categoria, id_editora) VALUES (2, '1984', '0987654321', 2, 1, 2)")
    cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, isbn, id_autor, id_categoria, id_editora) VALUES (3, 'O Processo', '1122334455', 3, 1, 3)")
    cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, isbn, id_autor, id_categoria, id_editora) VALUES (4, 'O Pequeno Príncipe', '5566778899', 4, 1, 4)")

    conn.commit()

# Função para cadastrar livro
def cadastrar_livro():
    titulo = input("Título: ")
    isbn = input("ISBN: ")
    id_autor = int(input("ID do Autor: "))
    id_categoria = int(input("ID da Categoria: "))
    id_editora = int(input("ID da Editora: "))
    cursor.execute('INSERT INTO Livro (titulo, isbn, id_autor, id_categoria, id_editora) VALUES (?, ?, ?, ?, ?)', (titulo, isbn, id_autor, id_categoria, id_editora))
    conn.commit()
    print("Livro cadastrado com sucesso!")

# Função para cadastrar autor
def cadastrar_autor():
    nome_autor = input("Nome do Autor: ")
    cursor.execute('INSERT INTO Autor (nome_autor) VALUES (?)', (nome_autor,))
    conn.commit()
    print("Autor cadastrado com sucesso!")

# Função para cadastrar categoria
def cadastrar_categoria():
    nome_categoria = input("Nome da Categoria: ")
    cursor.execute('INSERT INTO Categoria (nome_categoria) VALUES (?)', (nome_categoria,))
    conn.commit()
    print("Categoria cadastrada com sucesso!")

# Função para cadastrar editora
def cadastrar_editora():
    nome_editora = input("Nome da Editora: ")
    pais_publicacao = input("País de Publicação: ")
    cursor.execute('INSERT INTO Editora (nome_editora, pais_publicacao) VALUES (?, ?)', (nome_editora, pais_publicacao))
    conn.commit()
    print("Editora cadastrada com sucesso!")

# Função para imprimir todos os registros de uma tabela
def imprimir_todos(table):
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    if table == "Livro":
        print("\nTodos os livros:")
        print("ID | Título | ISBN | ID do Autor | ID da Categoria | ID da Editora")
    elif table == "Autor":
        print("\nTodos os autores:")
        print("ID | Nome")
    elif table == "Categoria":
        print("\nTodas as categorias:")
        print("ID | Nome")
    elif table == "Editora":
        print("\nTodas as editoras:")
        print("ID | Nome | País de Publicação")
    
    for row in rows:
        print(row)
    print("\n" + "-"*40)  # Linha de separação para clareza

# Função para imprimir livros por autor
def imprimir_livros_por_autor():
    id_autor = int(input("ID do Autor: "))
    cursor.execute('''
    SELECT * FROM Livro
    WHERE id_autor = ?
    ''', (id_autor,))
    rows = cursor.fetchall()
    if rows:
        print("\nLivros publicados pelo autor:")
        print("ID | Título | ISBN | ID do Autor | ID da Categoria | ID da Editora")
        for row in rows:
            print(row)
    else:
        print("Nenhum livro encontrado para o autor fornecido.")
    print("\n" + "-"*40)  # Linha de separação para clareza

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar livro")
    print("2. Cadastrar autor")
    print("3. Cadastrar categoria")
    print("4. Cadastrar editora")
    print("5. Imprimir todos os livros")
    print("6. Imprimir todos os autores")
    print("7. Imprimir todas as categorias")
    print("8. Imprimir todas as editoras")
    print("9. Imprimir todos os livros publicados por um autor")
    print("10. Sair")
    return input("Escolha uma opção: ")

# Inserir dados iniciais
plot_bd()

# Loop principal do programa
while True:
    escolha = exibir_menu()

    if escolha == '1':
        cadastrar_livro()
    elif escolha == '2':
        cadastrar_autor()
    elif escolha == '3':
        cadastrar_categoria()
    elif escolha == '4':
        cadastrar_editora()
    elif escolha == '5':
        imprimir_todos('Livro')
    elif escolha == '6':
        imprimir_todos('Autor')
    elif escolha == '7':
        imprimir_todos('Categoria')
    elif escolha == '8':
        imprimir_todos('Editora')
    elif escolha == '9':
        imprimir_livros_por_autor()
    elif escolha == '10':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
conn.close()
