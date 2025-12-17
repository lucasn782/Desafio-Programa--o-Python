import secrets

def gerar_senha(qtd_palavras, caminho_arquivo='diceware.wordlist.pt.txt'):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()[3:7779]
        lista_palavras = [line.split()[1] for line in linhas]
        
    palavras = [secrets.choice(lista_palavras) for i in range(qtd_palavras)]
    return ' '.join(palavras)
