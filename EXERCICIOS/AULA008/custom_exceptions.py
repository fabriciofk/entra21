class MinorError(Exception):
    """Age under 18.

    Attributes:
        message: Explanation of the error
    """
    def __init__(self, message: str = "Idade menor do que 18 anos.") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'Falha ao cadastrar: {self.message}'


class InvalidAddress(Exception):
    """Invalid address fields.

        Attributes:
            message: Explanation of the error.
    """

    def __init__(self, message: str = "Dados de endereço inválidos.") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f'Falha ao cadastrar: {self.message}'
