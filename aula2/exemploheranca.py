class Animal:
    
    def __init__(self, nome, idade, peso, raca, especie):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raca = raca
        self.especie = especie
    
    
    
    def __str__(self):
        return 'SOM'
    
    
    
class Cachorro(Animal):
    
    def __str__(self):
        return 'Au Au'
    
class Gato(Animal):
    
    def __str__(self):
        return 'Miau'
    
class Porco(Animal):
    
    def __str__(self):
        return 'Ronc'
    
cachorro1 = Cachorro ('Rex', 2, '5kg', 'Pastor Alemão', 'mamífero')
gato1 = Gato ('Ace', 2, '2kg', 'sem', 'mamífero')
porco1 = Porco ('Pepa', 4, '25kg', 'sem', 'mamífero')
    
print(gato1)   
print(gato1.nome)