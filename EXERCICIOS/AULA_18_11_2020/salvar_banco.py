import sqlite3


def database_operations(query: str, data: tuple = None) -> list:
    try:
        with sqlite3.connect('database.db') as conn:
            # Instanciando o cursor
            cursor = conn.cursor()

            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)

            # Commit no banco
            conn.commit()

            return cursor.fetchall()
    except Exception as err:
        print(err)


query_create_veiculo = """
    CREATE TABLE IF NOT EXISTS veiculo (
            id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            placa TEXT NOT NULL,                
            proprietario TEXT NOT NULL,
            num_portas INTEGER NOT NULL,
            cor TEXT NOT NULL,
            km_rodados REAL NOT NULL,
            qtd_passageiros INTEGER NOT NULL,
            motor TEXT NOT NULL,
            combustivel TEXT NOT NULL,
            meio_locomocao TEXT NOT NULL
        );
"""

query_create_pessoa = """
    CREATE TABLE IF NOT EXISTS pessoa (
            id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,           
            data_nascimento TEXT NOT NULL,
            cpf TEXT NOT NULL,
            endereco TEXT NOT NULL,
            salario REAL NOT NULL,
            profissao TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            nome_responsavel TEXT NOT NULL,
            sexo TEXT NOT NULL,
            naturalidade TEXT NOT NULL,
            nacionalidade TEXT NOT NULL
        );           
"""

# Criando a tabela carro
database_operations(query_create_veiculo)

# Criando a tabela pessoa
database_operations(query_create_pessoa)

