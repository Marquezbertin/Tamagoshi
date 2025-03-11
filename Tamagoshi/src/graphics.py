def draw_pet(pet):
    if pet.saude <= 0 or pet.fome >= 100:
        print("""
    ------------------------------------------
     __         __
    /  \.-" "-./  \.
    \    -   -    /
     |   X   X   |
     \  .-'''-.  /
      '-\__Y__/-'
         `---`
            """)
    else:
        print(f"""
    ------------------------------------------
     __         __
    /  \.-" "-./  \.
    \    -   -    /
     |   o   o   |
     \  .-'''-.  /
      '-\__Y__/-'
         `---`
            """)

def display_interface(pet):
    print(f"\nO bichinho {pet.nome} está aqui! Personalidade: {pet.personalidade}")
    print(f"Fome: {pet.fome}, Saúde: {pet.saude}, Humor: {pet.humor}, Dinheiro: {pet.dinheiro}")

def show_actions():
    actions = [
        "1 - Alimentar (-10 de fome)",
        "2 - Dormir (+10 de saúde)",
        "3 - Brincar (Melhora humor)",
        "4 - Comprar comida (-10 moedas)",
        "5 - Comprar remédio (-20 moedas)",
        "6 - Treinar (Evoluir bichinho)",
        "7 - Visualizar informações"
    ]
    
    print("\nEscolha uma ação:")
    for action in actions:
        print(action)