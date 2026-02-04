import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida_maxima = vida 
        self.vida = vida
        
    def aplicar_critico(self, dano_base):
        # Atividade 1: Chance de 15% de dano dobrado
        if random.random() <= 0.15:
            print(f"CRÍTICO! {self.nome} causou dano dobrado!")
            return dano_base * 2
        return dano_base

    def curar(self):
        # Atividade 2: Recupera 25 de vida (quantidade fixa)
        if self.esta_vivo():
            self.vida += 25
            if self.vida > self.vida_maxima:
                self.vida = self.vida_maxima
            print(f"{self.nome} usou poção. Vida atual: {self.vida}")

    def sofrer_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} sofreu {dano} de dano. Vida: {self.vida}")
        
    def esta_vivo(self):
        return self.vida > 0

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} ataca com espada!")
        return self.aplicar_critico(self.forca)

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.nome} lança magia! Mana: {self.mana}")
            return self.aplicar_critico(25)
        else:
            print(f"{self.nome} usa ataque fraco (sem mana).")
            return self.aplicar_critico(5)

class Arqueiro(Personagem):
    def __init__(self, nome, vida, flechas):
        super().__init__(nome, vida)
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0:
            self.flechas -= 5
            print(f"{self.nome} atira flechas! Restantes: {self.flechas}")
            return self.aplicar_critico(15)
        else:
            print(f"{self.nome} está sem flechas!")
            return self.aplicar_critico(5)

def grande_batalha(jogadores):
    turno = 1
    # Atividade 3: Batalha em turnos usando a lista
    while sum(1 for p in jogadores if p.esta_vivo()) > 1:
        print(f"\n--- Turno {turno} ---")
        
        for atacante in jogadores:
            if not atacante.esta_vivo():
                continue
            
            alvos_vivos = [p for p in jogadores if p != atacante and p.esta_vivo()]
            if not alvos_vivos:
                break
            
            # Personagem decide curar se estiver com pouca vida (ex: menos de 30)
            if atacante.vida < 30:
                atacante.curar()
            else:
                alvo = random.choice(alvos_vivos)
                dano = atacante.atacar()
                alvo.sofrer_dano(dano)
            
            if not alvo.esta_vivo():
                print(f"{alvo.nome} foi derrotado!")

        turno += 1

    # Atividade 4: Mostrar vencedor final
    
    vencedor = next(p for p in jogadores if p.esta_vivo())
    print(f"\nVencedor: {vencedor.nome} | Vida Restante: {vencedor.vida}")

#  Execução do Teste

p1 = Guerreiro('Marcos', 150, 20)
p2 = Mago('José', 100, 80)
p3 = Arqueiro('João', 120, 15)

lista_personagens = [p1, p2, p3]
grande_batalha(lista_personagens)
