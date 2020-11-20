import sqlite3


def banco_operacoes(query: str, dados: tuple = None) -> list:
    """
    Executa a query informada no banco de dados, se houver dados passados
    como parâmetro, a query é executado com esses dados.

    Args:
        query: query do banco.
        dados: dados utilizados na query.

    Returns:
        Uma lista com os registros presentes no cursor.
    """
    try:
        with sqlite3.connect('database.db') as conn:
            # Instanciando o cursor
            cursor = conn.cursor()

            if dados:
                cursor.execute(query, dados)
                conn.commit()
            else:
                cursor.execute(query)

            return cursor.fetchall()
    except Exception as err:
        print(f'Erro: {err}')
        print('Não foi possível realizar a operação.')


# ========================================================================== #
#                  QUERIES PARA CRIAR AS TABELAS NO BANCO                    #
# ========================================================================== #
query_create_veiculo = """
    CREATE TABLE IF NOT EXISTS veiculo (
            id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            placa TEXT NOT NULL,                
            id_pessoa INTEGER NOT NULL,
            num_portas INTEGER NOT NULL,
            cor TEXT NOT NULL,
            km_rodados REAL NOT NULL,
            qtd_passageiros INTEGER NOT NULL,
            motor TEXT NOT NULL,
            combustivel TEXT NOT NULL,
            meio_locomocao TEXT NOT NULL,
            FOREIGN KEY(id_pessoa)
                REFERENCES pessoa(id_pessoa)
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

# ========================================================================== #
#                           CRIANDO AS TABELAS                               #
# ========================================================================== #
banco_operacoes(query_create_pessoa)
banco_operacoes(query_create_veiculo)
