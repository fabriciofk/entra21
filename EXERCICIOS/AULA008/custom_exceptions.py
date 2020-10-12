class MinorError(Exception):
    def __init__(self, message: str = 'Menor de idade.') -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Erro: {self.message}'


class InvalidFields(Exception):
    def __init__(self, message: str = 'Dados inválidos'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Erro: {self.message}'
