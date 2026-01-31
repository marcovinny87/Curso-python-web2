import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        
    def atacar(self):
        return 10
    
    # --- NOVO MÉTODO ---
    def ataque_critico(self):
       # Gera um dano aleatório entre 20 e 40
        dano = random.randint(20, 40)
        print(f"CRÍTICO! {self.nome} desferiu um golpe especial de {dano} de dano!")
        return dano
    # -------------------

    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} sofreu {dano} de dano. Vida agora: {self.vida}')
        
    def esta_vivo(self):
        return self.vida > 0
    
    
# Criar 2 objetos e testar métodos
    
class Guerreiro (Personagem): #Herda os atributos
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca   # Adiciona algo exclusivo do Guerreiro
    def atacar(self):
            print(f'{self.nome} ataca com espada!')
            return self.forca
       
       

    
    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} sofreu {dano} de dano. Vida agora: {self.vida}')
        
    def esta_vivo(self):
        return self.vida > 0
    
    
    
        
class Mago (Personagem): #Herda os atributos
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana     # Adiciona algo exclusivo do Mago
        
    
    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f'{self.nome} lança magia! Mana restante: {self.mana}')
            return 25
        else: print(f'{self.nome} usa ataque fraco! Mana insuficiente.')
        return 5
    
    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} sofreu {dano} de dano. Vida agora: {self.vida}')
        
    def esta_vivo(self):
        return self.vida > 0
    


class Arqueiro (Personagem): #Herda os atributos
    def __init__(self, nome, vida, flechas):
        super().__init__(nome, vida)
        self.flechas = flechas     # Adiciona algo exclusivo do Arqueiro
    
    def atacar(self):
      
        if self.flechas > 0:
            self.flechas -= 5
            print(f'{self.nome} atira flecha(s)! Flecha(s) restante(s): {self.flechas}')
            return 10
        else: print(f'{self.nome} número de flechas insuficiente.')
        return 20
    
    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} sofreu {dano} de dano. Vida agora: {self.vida}')
        
    def esta_vivo(self):
        return self.vida > 0



def combate(personagem1, personagem2):
    turno = 1
    
    while personagem1.esta_vivo() and personagem2.esta_vivo():
        print(f'\n--- Turno {turno} ---')
    
        dano = personagem1.atacar()
        personagem2.sofrer_dano(dano)
    
        if not personagem2.esta_vivo():
            print(f'{personagem2.nome} foi derrotado!')
            break
       
        dano = personagem2.atacar()
        personagem1.sofrer_dano(dano)
        
        if not personagem1.esta_vivo():
            print(f'{personagem1.nome} foi derrotado!')
            break
        
        turno +=1
    
    

# Testando objetos e métodos


personagem1 = Guerreiro ('Marcos', 150, 20)
# print(personagem1.sofrer_dano(5))
# print(personagem1.esta_vivo())

personagem2 = Mago ('José', 100, 80)
# print(personagem2.sofrer_dano(10))
# print(personagem2.esta_vivo())

# print(personagem1.atacar())
# print(personagem2.sofrer_dano(10))
# print(personagem2.esta_vivo())

# print(personagem2. atacar())
# print(personagem1.sofrer_dano(5))
personagem3 = Arqueiro ('João', 120, 50)
# print(personagem3. atacar())
# print(personagem1.sofrer_dano(5))



# Chamando o novo método herdado
dano_especial = personagem1.ataque_critico() 
personagem2.sofrer_dano(dano_especial)

#Testando combate entre Guerreiro
combate(personagem1, personagem2)

combate(personagem3, personagem2)