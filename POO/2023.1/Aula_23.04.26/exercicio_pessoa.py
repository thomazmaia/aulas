import datetime

class Data:
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        #self.dia = datetime.date.today().day
        #self.mes = datetime.date.today().month
        #self.ano = datetime.date.today().year

    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.ano}"

class Contato:
    def __init__(self, tel, cel, email) -> None:
        self.tel = tel
        self.cel = cel
        self.email = email
    
class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep) -> None:
        self.logradouro = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.data_nascimento = Data(6, 9, 2020)
        self.endereco = Endereco("Rua x", 123, "Bairro", "Eusébio", "CE", 61000000)
        self.contato = Contato("1234-5678", "9999-9999", "artur@gmail.com")



p1 = Pessoa("Artur")

del p1

print(p1.data_nascimento)