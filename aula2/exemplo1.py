#Crie uma classe: Mini mundo Escola

#professor aluno   diretor

class Professor:
    def __init__(self, nome):
        self.nome = nome
        
        
    def apresentar(self):
        print(f"nome:{self.nome}")
        
        
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
               

    def apresentar(self):
        print(f"nome:{self.nome}, matricula: {self.matricula}")
        
        
class Diretor:
    def __init__(self, nome):
        self.nome = nome
        

    def apresentar(self):
        print(f"nome:{self.nome}")


professor1 = Professor("Gregory")
aluno1 = Aluno("Marcos", "5479837")
diretor1 = Diretor("Sandro")

print(vars(professor1))
print(aluno1.nome, aluno1.matricula)
print(aluno1.matricula)





