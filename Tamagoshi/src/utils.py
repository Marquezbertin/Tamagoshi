def gerar_evento_aleatorio():
    eventos = ["doença", "problema financeiro", "evento positivo"]
    return random.choice(eventos)

def salvar_progresso_em_json(progresso, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(progresso, arquivo)

def carregar_progresso_de_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None

def limitar_valor(valor, minimo, maximo):
    return max(minimo, min(maximo, valor))