import json
import os

class Item:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def to_dict(self):
        return {"nome": self.nome, "valor": self.valor}

class Mercado:
    def __init__(self):
        self.itens_comprados = []
        self.limite_cliente = 0.0
        self.tabela_precos = {
            "1": {"nome": "Feijão", "preco": 5.00},
            "2": {"nome": "Arroz", "preco": 22.50},
            "3": {"nome": "Açúcar", "preco": 3.50},
            "4": {"nome": "Sal", "preco": 2.00},
            "5": {"nome": "Café", "preco": 25.00},
            "6": {"nome": "Óleo", "preco": 7.00}
        }

    def comprar_produto(self):
        print("\n--- PRODUTOS DISPONÍVEIS ---")
        for codigo, info in self.tabela_precos.items():
            print(f"{codigo} - {info['nome']}: R$ {info['preco']}")
        
        escolha = input("\nDigite o número do produto que deseja comprar: ")
        
        if escolha in self.tabela_precos:
            produto = self.tabela_precos[escolha]
            novo_item = Item(produto['nome'], produto['preco'])
            self.itens_comprados.append(novo_item)
            print(" Item adicionado!")
            self.salvar_dados()
        else:
            print(" Opção inválida!")

    def ver_relatorio(self):
        print("\n=== RELATÓRIO ===")
        
        if not self.itens_comprados:
            print("Carrinho vazio.")
        else:
            total = 0
            
            for item in self.itens_comprados:
                print(item.nome, "R$", item.valor)
                total += item.valor
            
            print("------------------")
            print("TOTAL GASTO: R$", total)
            print("LIMITE: R$", self.limite_cliente)
            
            if total > self.limite_cliente:
                print(" AVISO: Limite excedido!")
            else:
                print(" Dentro do limite.")
        print("==================")

    def finalizar_e_limpar(self):
        self.itens_comprados = []
        self.limite_cliente = 0.0
        self.salvar_dados()
        print("\n Carrinho limpo!")

    def salvar_dados(self):
        dados = {
            "limite": self.limite_cliente,
            "itens": [item.to_dict() for item in self.itens_comprados]
        }
        with open("caixa.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        if os.path.exists("caixa.json"):
            with open("caixa.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, dict):
                    self.limite_cliente = dados.get("limite", 0.0)
                    self.itens_comprados = [Item(i["nome"], i["valor"]) for i in dados.get("itens", [])]
                else:
                    self.itens_comprados = [Item(i["nome"], i["valor"]) for i in dados]

def menu():
    caixa = Mercado()
    caixa.carregar_dados()

    if caixa.limite_cliente == 0:
        try:
            caixa.limite_cliente = float(input("Quanto você pretende gastar? R$ "))
            caixa.salvar_dados()
        except ValueError:
            caixa.limite_cliente = 0.0

    while True:
        print("\n1 - Comprar | 2 - Relatório | 3 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            caixa.comprar_produto()
        elif opcao == "2":
            caixa.ver_relatorio()
        elif opcao == "3":
            caixa.finalizar_e_limpar()
            print("Compra Finalizada!")
            break

if __name__ == "__main__":
    menu()