class Endereco:
    def __init__(self, logradouro, numero, bairro, cep, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado


class Pessoa:
    def __init__(self, nome, data_nascimento, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
