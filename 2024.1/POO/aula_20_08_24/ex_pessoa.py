class Data:
    def __init__(self, d:int, m:int, a:int) -> None:
        self.dia = d
        self.mes = m
        self.ano = a


class Endereco:
    def __init__(self, log:str, num:int, bairro:str, cidade:str, estado:str, cep:int) -> None:
        self.logradouro = log
        self.numero = num
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


class Contato:
    def __init__(self, tel:str, cel:str, mail:str) -> None:
        self.tel = tel
        self.cel = cel
        self.email = mail

class Pessoa:
    def __init__(self, nome:str, tel:str, cel:str, email:str) -> None:
        self.nome = nome
        self.data_nascimento = None
        self.endereco = None
        self.contato = Contato(cel, tel, email)

    def set_data_nascimento(self, dia, mes, ano):
        self.data_nascimento = Data(dia, mes, ano)

    def set_endereco(self, log, num, bairro, cid, est, cep):
        self.endereco = Endereco(log, num, bairro, cid, est, cep)        


P1 = Pessoa("Xico", "9900-0100", "9900-0100", "xico@gmail.com")
P1.set_data_nascimento(10, 10, 2000)
P1.set_endereco("Rua dos anzois", "123", "Centro", "Maranguape", "CE", "60.000-00")

del P1

P2 = Pessoa("Ze", "9911-1991", "9911-1991", "ze@gmail.com")