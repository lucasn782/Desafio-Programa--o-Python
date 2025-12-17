def ordenando_palavras(palavras):
    return ' '.join(sorted(palavras.split(), key=str.casefold))
