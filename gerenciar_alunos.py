import sqlite3

# Conectar ao banco de dados SQLite (ou criar se não existir)
conn = sqlite3.connect('universidade.db')
cursor = conn.cursor()

# Apagar tabelas antigas, se existirem
cursor.execute('DROP TABLE IF EXISTS Aluno_Disciplina')
cursor.execute('DROP TABLE IF EXISTS Aluno')
cursor.execute('DROP TABLE IF EXISTS Disciplina')

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Aluno (
    id_aluno INTEGER PRIMARY KEY,
    nome_aluno TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplina (
    id_disciplina INTEGER PRIMARY KEY,
    nome_disciplina TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Aluno_Disciplina (
    id_aluno INTEGER,
    id_disciplina INTEGER,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES Aluno (id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplina (id_disciplina)
)
''')

# Funções para manipular o banco de dados
def cadastrar_aluno(nome):
    cursor.execute('INSERT INTO Aluno (nome_aluno) VALUES (?)', (nome,))
    conn.commit()

def cadastrar_disciplina(nome):
    cursor.execute('SELECT * FROM Disciplina WHERE nome_disciplina = ?', (nome,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO Disciplina (nome_disciplina) VALUES (?)', (nome,))
        conn.commit()
    else:
        print(f'A disciplina {nome} já está cadastrada.')

def matricular_aluno(id_aluno, id_disciplina):
    cursor.execute('SELECT * FROM Aluno_Disciplina WHERE id_aluno = ? AND id_disciplina = ?', (id_aluno, id_disciplina))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO Aluno_Disciplina (id_aluno, id_disciplina) VALUES (?, ?)', (id_aluno, id_disciplina))
        conn.commit()
    else:
        print(f'O aluno {id_aluno} já está matriculado na disciplina {id_disciplina}.')

def imprimir_alunos():
    cursor.execute('SELECT * FROM Aluno')
    print("\nAlunos:")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Nome: {row[1]}")

def imprimir_disciplinas():
    cursor.execute('SELECT * FROM Disciplina')
    print("\nDisciplinas:")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Nome: {row[1]}")

def imprimir_disciplinas_de_aluno(id_aluno):
    cursor.execute('''
    SELECT Disciplina.nome_disciplina FROM Disciplina
    JOIN Aluno_Disciplina ON Disciplina.id_disciplina = Aluno_Disciplina.id_disciplina
    WHERE Aluno_Disciplina.id_aluno = ?
    ''', (id_aluno,))
    print(f"\nDisciplinas do aluno com ID {id_aluno}:")
    for row in cursor.fetchall():
        print(f"Nome: {row[0]}")

def imprimir_alunos_de_disciplina(id_disciplina):
    cursor.execute('''
    SELECT Aluno.nome_aluno FROM Aluno
    JOIN Aluno_Disciplina ON Aluno.id_aluno = Aluno_Disciplina.id_aluno
    WHERE Aluno_Disciplina.id_disciplina = ?
    ''', (id_disciplina,))
    print(f"\nAlunos da disciplina com ID {id_disciplina}:")
    for row in cursor.fetchall():
        print(f"Nome: {row[0]}")

# Inserir dados de exemplo
cadastrar_aluno('Alice')
cadastrar_aluno('Bob')
cadastrar_aluno('Carol')

cadastrar_disciplina('Matemática')
cadastrar_disciplina('Física')
cadastrar_disciplina('Química')
cadastrar_disciplina('Biologia')

matricular_aluno(1, 1)  # Alice em Matemática
matricular_aluno(1, 2)  # Alice em Física
matricular_aluno(2, 3)  # Bob em Química
matricular_aluno(3, 4)  # Carol em Biologia
matricular_aluno(3, 3)  # Carol em Química
matricular_aluno(3, 1)  # Carol em Matemática

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar aluno")
    print("2. Cadastrar disciplina")
    print("3. Matricular aluno em disciplina")
    print("4. Imprimir todos os alunos")
    print("5. Imprimir todas as disciplinas")
    print("6. Imprimir todas as disciplinas de um aluno")
    print("7. Imprimir todos os alunos de uma disciplina")
    print("8. Sair")
    return input("Escolha uma opção: ")

# Loop principal do programa
while True:
    escolha = exibir_menu()

    if escolha == '1':
        nome_aluno = input("Digite o nome do aluno: ")
        cadastrar_aluno(nome_aluno)
    elif escolha == '2':
        nome_disciplina = input("Digite o nome da disciplina: ")
        cadastrar_disciplina(nome_disciplina)
    elif escolha == '3':
        id_aluno = int(input("Digite o ID do aluno: "))
        id_disciplina = int(input("Digite o ID da disciplina: "))
        matricular_aluno(id_aluno, id_disciplina)
    elif escolha == '4':
        imprimir_alunos()
    elif escolha == '5':
        imprimir_disciplinas()
    elif escolha == '6':
        id_aluno = int(input("Digite o ID do aluno: "))
        imprimir_disciplinas_de_aluno(id_aluno)
    elif escolha == '7':
        id_disciplina = int(input("Digite o ID da disciplina: "))
        imprimir_alunos_de_disciplina(id_disciplina)
    elif escolha == '8':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
conn.close()
