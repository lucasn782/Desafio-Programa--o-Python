import re

def eh_palindromo(frase):
    correta = ''.join(re.findall(r'[a-z]+', frase.lower()))
    revertida = correta[::-1]
    return correta == revertida