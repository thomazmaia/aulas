from app import db

class Pessoa(db.Model):  # Herda da classe "db.Model"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.nome