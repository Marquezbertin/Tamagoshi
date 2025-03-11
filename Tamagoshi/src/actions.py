def alimentar(bichinho):
    if bichinho.dinheiro >= 10:
        bichinho.alterar_fome(-10)
        bichinho.dinheiro -= 10
        print(f"Você alimentou {bichinho.nome}!")
    else:
        print("Você não tem dinheiro suficiente para comprar comida.")

def brincar(bichinho):
    if bichinho.dinheiro >= 5:
        bichinho.brincar()
        print(f"Você brincou com {bichinho.nome}!")
    else:
        print("Você não tem dinheiro suficiente para brincar.")

def dormir(bichinho):
    bichinho.alterar_saude(+10)
    print(f"{bichinho.nome} dormiu e recuperou saúde!")

def comprar_remedio(bichinho):
    if bichinho.dinheiro >= 20:
        bichinho.comprar_remedio()
        print(f"Você comprou remédio para {bichinho.nome}!")
    else:
        print("Você não tem dinheiro suficiente para comprar remédio.")

def treinar(bichinho):
    if bichinho.dinheiro >= 15:
        bichinho.treinar()
        print(f"{bichinho.nome} treinou e ganhou experiência!")
    else:
        print("Você não tem dinheiro suficiente para treinar.")

def visualizar_informacoes(bichinho):
    bichinho.visualizar_informacoes()