import random
import json
from graphics import mostrar_desenho
from actions import alterar_fome, alterar_saude, brincar, comprar_comida, comprar_remedio, treinar, visualizar_informacoes

class BichinhoVirtual:
    def __init__(self, nome, dinheiro=100):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
        self.humor = self.saude - self.fome
        self.dinheiro = dinheiro
        self.personalidade = random.choice(['brincalhão', 'tímido', 'amigável', 'agressivo'])
        self.desafios_completados = 0
    
    def mostrar_desenho(self):
        mostrar_desenho(self.saude, self.fome)

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        
    def alterar_idade(self):
        self.idade += 1
        self.verificar_eventos_aleatorios()
        
    def atualizar_humor(self):
        self.humor = self.saude - self.fome
        
    def verificar_eventos_aleatorios(self):
        chance = random.randint(1, 100)
        if chance <= 20:
            evento = random.choice(["doença", "problema financeiro", "evento positivo"])
            if evento == "doença":
                print(f"{self.nome} ficou doente! Perdeu 10 de saúde.")
                alterar_saude(self, -10)
            elif evento == "problema financeiro":
                print(f"{self.nome} teve um problema financeiro! Perdeu 20 moedas.")
                self.dinheiro -= 20
            elif evento == "evento positivo":
                print(f"{self.nome} teve um evento positivo! Ganhou 20 moedas.")
                self.dinheiro += 20
        
    def interagir(self):
        self.mostrar_desenho()
        print(f"\nO bichinho {self.nome} está aqui! Personalidade: {self.personalidade}")
        print(f"Fome: {self.fome}, Saúde: {self.saude}, Humor: {self.humor}, Dinheiro: {self.dinheiro}")
        
        acoes = [
            "1 - Alimentar (-10 de fome)",
            "2 - Dormir (+10 de saúde)",
            "3 - Brincar (Melhora humor)",
            "4 - Comprar comida (-10 moedas)",
            "5 - Comprar remédio (-20 moedas)",
            "6 - Treinar (Evoluir bichinho)",
            "7 - Visualizar informações"
        ]
        
        print("\nEscolha uma ação:")
        for acao in acoes:
            print(acao)
            
        escolha = input("\nSua escolha: ")
        
        if escolha == "1":
            alterar_fome(self, -10)
            print("Você alimentou o bichinho!")
        elif escolha == "2":
            alterar_saude(self, +10)
            print("Você fez o bichinho dormir!")
        elif escolha == "3":
            brincar(self)
            print("Você brincou com o bichinho!")
        elif escolha == "4":
            comprar_comida(self)
        elif escolha == "5":
            comprar_remedio(self)
        elif escolha == "6":
            treinar(self)
        elif escolha == "7":
            visualizar_informacoes(self)
        else:
            print("Escolha inválida. Tente novamente.")
    
    def verificar_desafios(self):
        if self.idade >= 5:
            print(f"Desafio cumprido! {self.nome} atingiu 5 anos de idade!")
            self.desafios_completados += 1
    
    def salvar_progresso(self, nome_arquivo):
        progresso = {
            "nome": self.nome,
            "fome": self.fome,
            "saude": self.saude,
            "idade": self.idade,
            "humor": self.humor,
            "dinheiro": self.dinheiro,
            "personalidade": self.personalidade,
            "desafios_completados": self.desafios_completados
        }
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(progresso, arquivo)
        print("Progresso salvo com sucesso!")
    
    def carregar_progresso(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                progresso = json.load(arquivo)
                self.nome = progresso["nome"]
                self.fome = progresso["fome"]
                self.saude = progresso["saude"]
                self.idade = progresso["idade"]
                self.humor = progresso["humor"]
                self.dinheiro = progresso["dinheiro"]
                self.personalidade = progresso["personalidade"]
                self.desafios_completados = progresso["desafios_completados"]
                print("Progresso carregado com sucesso!")
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado. Iniciando um novo jogo.")
    
def iniciar_jogo():
    print("Bem-vindo ao jogo Tamagoshi!")
    nome_bichinho = input("Qual o nome do seu bichinho? ")
    bichinho = BichinhoVirtual(nome_bichinho)
    
    while bichinho.saude > 0 and bichinho.fome < 100:
        bichinho.alterar_idade()
        bichinho.interagir()
        bichinho.verificar_desafios()
        
        salvar = input("Deseja salvar o progresso? (s/n): ")
        if salvar.lower() == 's':
            nome_arquivo = input("Digite o nome do arquivo para salvar o progresso: ")
            bichinho.salvar_progresso(nome_arquivo)
        
        continuar = input("Deseja continuar jogando? (s/n): ")
        if continuar.lower() == 'n':
            print("Obrigado por jogar! Até mais!")
            break
    
    print(f"\nSeu bichinho {bichinho.nome} morreu aos {bichinho.idade} anos. :(")

if __name__ == "__main__":
    iniciar_jogo()