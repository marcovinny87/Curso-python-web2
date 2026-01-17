class Pessoa:
    def __init__(self, nome, idade, pet, cpf, cartao):
       self.nome = nome
       self.idade = idade
       self.pet = pet
       self.cpf = cpf
       self.cartao = cartao
       
            
    def apresentar(self):
        print(f"nome:{self.nome}, idade:{self.idade}, pet:{self.pet}, cpf:{self.cpf}, cartao: {self.cartao}")
        
        pessoa1 = Pessoa("Gregory", 20, "Não tem", "012345678998", "132654345890")
        pessoa2 = Pessoa("Ericson", 18, "Tem gato", "45678934578", "54468546546")
        pessoa3 = Pessoa("Ana", 19, "Tem cachorro", "495594032033, 23838393020239") 
        pessoa4 = Pessoa("Luiza", 22, "Não tem", "3930943049495", "3030439493932")
        
        
        print(vars(pessoa1))
        print(pessoa2.nome)