from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Usuário: {self.nome}"
    
    def falar(self):
        print(f"{self.nome} está falando")
