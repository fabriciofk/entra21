import sqlite3


def database_operations(connection_name: str, query: str, data: tuple = None) -> None:
    try:
        with sqlite3.connect(connection_name) as conn:
            # Instanciando o cursor
            cursor = conn.cursor()
            if data:
                cursor.execute(query, data)            
    except Exception as err:
        print(err)

if __name__ == "__main__":
    query_create_carro = """
        CREATE TABLE IF NOT EXISTS carro (
                id_carro INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                placa TEXT NOT NULL,                
                proprietario TEXT NOT NULL,
                num_portas INTEGER NOT NULL,
                cor TEXT NOT NULL,
                km_rodado REAL NOT NULL,
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
                data_nascimento DATE NOT NULL,
                cpf TEXT NOT NULL,
                endereco TEXT NOT NULL,
                salario REAL NOT NULL,
                profissao TEXT NOT NULL
            );            
    """

    # Criando a tabela carro
    database_operations('database.db', query_create_carro)

    # Criando a tabela pessoa
    database_operations('database.db', query_create_pessoa)

