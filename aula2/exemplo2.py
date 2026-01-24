class Pessoa:
    def __init__(self, nome, idade, cpf, ra, escola, funcao ):
       self.nome = nome
       self.idade = idade
       self.cpf = cpf
       self.ra = ra
       self.escola = escola
       self.funcao = funcao
       
    def __str__(self):
        return f'Olá, meu nome é {self.nome}'
       
aluno1 = Pessoa('Skill fucão', 35, '000000-10', '1345656', 'SENAC', 'Aluno')
diretor1 = Pessoa ('José', 19, '000000', '5433', 'SENAC', 'Diretor')
professor1 = Pessoa ('Pedro, 20')
print(vars(aluno1))
print(aluno1)