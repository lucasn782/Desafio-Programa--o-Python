import csv

def unir_csv(arquivos, caminho_arquivo_resultante):
    
    campos = []
    for arquivo in arquivos:
        with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
            campo = csv.DictReader(csv_entrada).fieldnames
            campos.extend(f for f in campo if f not in campos)
            
    with open(caminho_arquivo_resultante, 'w', encoding='utf-8', newline='') as csv_saida:
        escrita = csv.DictWriter(csv_saida, fieldnames=campos)
        escrita.writeheader()
        for arquivo in arquivos:
            with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
                leitor = csv.DictReader(csv_entrada)
                for linha in leitor:
                    escrita.writerow(linha)
                    