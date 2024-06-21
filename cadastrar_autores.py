import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('autores.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Autor (
    id_autor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT,
    data_nascimento TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Livro (
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano INTEGER,
    idioma TEXT,
    id_autor INTEGER,
    id_editora INTEGER,
    id_categoria INTEGER,
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor),
    FOREIGN KEY (id_editora) REFERENCES Editora(id_editora),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Editora (
    id_editora INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)
''')

# Inserção de dados iniciais

# Inserir categorias
cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome) VALUES (1, 'Ficção')")
cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome) VALUES (2, 'Não Ficção')")
cursor.execute("INSERT OR IGNORE INTO Categoria (id_categoria, nome) VALUES (3, 'Romance')")

# Inserir editoras
cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome) VALUES (1, 'Editora A')")
cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome) VALUES (2, 'Editora B')")
cursor.execute("INSERT OR IGNORE INTO Editora (id_editora, nome) VALUES (3, 'Editora C')")

# Inserir autores
cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome, nacionalidade, data_nascimento) VALUES (1, 'Fyodor Dostoyevsky', 'Russo', '1821-11-11')")
cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome, nacionalidade, data_nascimento) VALUES (2, 'George Orwell', 'Britânico', '1903-06-25')")
cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome, nacionalidade, data_nascimento) VALUES (3, 'Franz Kafka', 'Austríaco', '1883-07-03')")
cursor.execute("INSERT OR IGNORE INTO Autor (id_autor, nome, nacionalidade, data_nascimento) VALUES (4, 'Antoine de Saint-Exupéry', 'Francês', '1900-06-29')")

# Inserir livros
cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria) VALUES (1, 'Crime e Castigo', 1866, 'Russo', 1, 1, 1)")
cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria) VALUES (2, '1984', 1949, 'Inglês', 2, 2, 2)")
cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria) VALUES (3, 'O Processo', 1925, 'Alemão', 3, 3, 3)")
cursor.execute("INSERT OR IGNORE INTO Livro (id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria) VALUES (4, 'O Pequeno Príncipe', 1943, 'Francês', 4, 1, 1)")

# Funções para manipular o banco de dados

def cadastrar_autor():
    nome = input("Nome do Autor: ")
    nacionalidade = input("Nacionalidade: ")
    data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    cursor.execute('INSERT INTO Autor (nome, nacionalidade, data_nascimento) VALUES (?, ?, ?)', (nome, nacionalidade, data_nascimento))
    conn.commit()
    print("Autor cadastrado com sucesso.")

def cadastrar_livro():
    titulo = input("Título do Livro: ")
    ano = input("Ano de Publicação: ")
    idioma = input("Idioma: ")
    id_autor = int(input("ID do Autor: "))
    id_editora = int(input("ID da Editora: "))
    id_categoria = int(input("ID da Categoria: "))
    cursor.execute('INSERT INTO Livro (titulo, ano, idioma, id_autor, id_editora, id_categoria) VALUES (?, ?, ?, ?, ?, ?)', (titulo, ano, idioma, id_autor, id_editora, id_categoria))
    conn.commit()
    print("Livro cadastrado com sucesso.")

def editar_autor():
    id_autor = int(input("ID do Autor a ser editado: "))
    nome = input("Novo nome do Autor: ")
    nacionalidade = input("Nova nacionalidade: ")
    data_nascimento = input("Nova data de nascimento (AAAA-MM-DD): ")
    cursor.execute('UPDATE Autor SET nome=?, nacionalidade=?, data_nascimento=? WHERE id_autor=?', (nome, nacionalidade, data_nascimento, id_autor))
    conn.commit()
    print(f"Autor com ID {id_autor} atualizado.")

def editar_livro():
    id_livro = int(input("ID do Livro a ser editado: "))
    titulo = input("Novo título do Livro: ")
    ano = input("Novo ano de Publicação: ")
    idioma = input("Novo idioma: ")
    id_autor = int(input("Novo ID do Autor: "))
    id_editora = int(input("Novo ID da Editora: "))
    id_categoria = int(input("Novo ID da Categoria: "))
    cursor.execute('UPDATE Livro SET titulo=?, ano=?, idioma=?, id_autor=?, id_editora=?, id_categoria=? WHERE id_livro=?', (titulo, ano, idioma, id_autor, id_editora, id_categoria, id_livro))
    conn.commit()
    print(f"Livro com ID {id_livro} atualizado.")

def excluir_autor():
    id_autor = int(input("ID do Autor a ser excluído: "))
    cursor.execute('DELETE FROM Autor WHERE id_autor=?', (id_autor,))
    conn.commit()
    print(f"Autor com ID {id_autor} excluído com sucesso.")

def excluir_livro():
    id_livro = int(input("ID do Livro a ser excluído: "))
    cursor.execute('DELETE FROM Livro WHERE id_livro=?', (id_livro,))
    conn.commit()
    print(f"Livro com ID {id_livro} excluído com sucesso.")

def imprimir_todos_autores():
    cursor.execute('SELECT * FROM Autor')
    autores = cursor.fetchall()
    print("\nTodos os autores:")
    print("ID | Nome                    | Nacionalidade  | Data de Nascimento")
    print("-" * 60)
    for autor in autores:
        id_autor, nome, nacionalidade, data_nascimento = autor
        print(f"{id_autor:<3} | {nome:<22} | {nacionalidade:<14} | {data_nascimento}")
    print("-" * 60)

def imprimir_todos_livros():
    cursor.execute('SELECT * FROM Livro')
    livros = cursor.fetchall()
    print("\nTodos os livros:")
    print("ID | Título                | Ano  | Idioma   | ID do Autor | ID da Editora | ID da Categoria")
    print("-" * 82)
    for livro in livros:
        id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria = livro
        print(f"{id_livro:<3} | {titulo:<20} | {ano:<4} | {idioma:<8} | {id_autor:<11} | {id_editora:<13} | {id_categoria}")
    print("-" * 82)

def imprimir_livros_por_autor():
    id_autor = int(input("ID do Autor: "))
    cursor.execute('SELECT * FROM Livro WHERE id_autor=?', (id_autor,))
    livros = cursor.fetchall()
    if livros:
        print(f"\nLivros do Autor ID {id_autor}:")
        print("ID | Título                | Ano  | Idioma   | ID da Editora | ID da Categoria")
        print("-" * 72)
        for livro in livros:
            id_livro, titulo, ano, idioma, id_autor, id_editora, id_categoria = livro
            print(f"{id_livro:<3} | {titulo:<20} | {ano:<4} | {idioma:<8} | {id_editora:<13} | {id_categoria}")
    else:
        print(f"Nenhum livro encontrado para o Autor ID {id_autor}.")
    print("-" * 72)

# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar autor")
    print("2. Cadastrar livro")
    print("3. Editar autor")
    print("4. Editar livro")
    print("5. Excluir autor")
    print("6. Excluir livro")
    print("7. Imprimir todos os autores")
    print("8. Imprimir todos os livros")
    print("9. Imprimir todos os livros de um autor")
    print("10. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_autor()
    elif opcao == '2':
        cadastrar_livro()
    elif opcao == '3':
        editar_autor()
    elif opcao == '4':
        editar_livro()
    elif opcao == '5':
        excluir_autor()
    elif opcao == '6':
        excluir_livro()
    elif opcao == '7':
        imprimir_todos_autores()
    elif opcao == '8':
        imprimir_todos_livros()
    elif opcao == '9':
        imprimir_livros_por_autor()
    elif opcao == '10':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
conn.close()
