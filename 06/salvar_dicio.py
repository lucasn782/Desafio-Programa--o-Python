import pickle


def salvar_dicio(dict_para_exportar, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'wb') as arquivo:
        pickle.dump(dict_para_exportar, arquivo)
        
def carregar_dicio(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'rb') as arquivo:
        return pickle.load(arquivo)
        