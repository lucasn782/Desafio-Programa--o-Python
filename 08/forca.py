import os
import random


def escolher_palavra():
    palavras = {
        'curso': ["desafio", "python", "linkedin", "learning"],
        'frutas': ["banana", "laranja", "abacaxi", "melancia"],
        'paises': ["brasil", "argentina", "chile", "uruguai"],
        'animais': ["cachorro", "gato", "elefante", "girafa"]
    }
    tema = random.choice(list(palavras.keys()))
    palavra = random.choice(palavras[tema])
    return tema, palavra

def mostrar_tabuleiro(palavra, tema, tentativas, chutes):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"Tema {tema}\nPalavra: ", end="")
    for letra in palavra:
        print(letra if letra in chutes else "_", end=" ")
    print(f"\nTentativas restantes: {tentativas}")
    
def jogo_da_forca():
    tema, palavra = escolher_palavra()
    tentativas = len(palavra) - 1
    chutes = set()
    
    while tentativas > 0:
        mostrar_tabuleiro(palavra, tema, tentativas, chutes)
        chute = input("Escolha uma letra: ").lower()
        chutes.add(chute)
        
        if chute in palavra:
            print("Acertou!")
            if all(letra in chutes for letra in palavra):
                print(f"Parabéns, você adivinhou a palavra! A palavra era: {palavra}")
                break
        else:
            tentativas -= 1
            
        if tentativas == 0:
            print(f"Você perdeu! A palavra era: {palavra}")
            