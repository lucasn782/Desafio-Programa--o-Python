# Desafios de Programação Python

Este repositório contém três desafios de programação resolvidos em Python, cada um focando em um conceito diferente de manipulação de dados e algoritmos.

## 📋 Desafios Incluídos

### 1. **Fatores Primos** (`fatores.py`)
**Objetivo**: Encontrar todos os fatores primos de um número inteiro.

**Características**:
- Recebe um número inteiro como entrada
- Retorna uma lista com todos os fatores primos
- Algoritmo eficiente usando divisão sucessiva
- Exemplos:
  - `fatores_primos(630)` → `[2, 3, 3, 5, 7]`
  - `fatores_primos(13)` → `[13]`

### 2. **Verificador de Palíndromos** (`palindrome.py`)
**Objetivo**: Determinar se uma string é um palíndromo.

**Características**:
- Ignora pontuação, espaços e acentos
- Case-insensitive (trata maiúsculas/minúsculas igualmente)
- Usa expressões regulares para limpeza do texto
- Exemplos:
  - `eh_palindrome("Socorram-me, subi no ônibus em Marrocos!")` → `True`
  - `eh_palindrome("Olá mundo!")` → `False`

### 3. **Ordenador de Palavras** (`ordenando_palavras.py`)
**Objetivo**: Ordenar palavras em uma string alfabeticamente.

**Características**:
- Mantém a capitalização original das palavras
- Ignora maiúsculas/minúsculas durante a ordenação
- Usa `str.casefold()` para comparações robustas
- Exemplos:
  - `ordenando_palavras('maçã LARANJA banana')` → `'banana LARANJA maçã'`

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado

### Executando os desafios

1. **Clone o repositório**:
   ```bash
   git clone <repository-url>
   cd desafio-programacao-python
   ```

2. **Execute cada função**:

   **Fatores Primos**:
   ```python
   python -c "from fatores import fatores_primos; print(fatores_primos(630))"
   ```

   **Verificador de Palíndromos**:
   ```python
   python -c "from palindrome import eh_palindrome; print(eh_palindrome('Socorram-me, subi no ônibus em Marrocos!'))"
   ```

   **Ordenador de Palavras**:
   ```python
   python -c "from ordenando_palavras import ordenando_palavras; print(ordenando_palavras('maçã LARANJA banana'))"
   ```

3. **Ou use o interpretador Python interativo**:
   ```bash
   python
   >>> from fatores import fatores_primos
   >>> fatores_primos(630)
   [2, 3, 3, 5, 7]
   ```

## 📁 Estrutura do Projeto

```
desafio-programacao-python/
│
├── fatores.py              # Solução do desafio de fatores primos
├── palindrome.py           # Solução do desafio de palíndromos
├── ordenando_palavras.py   # Solução do desafio de ordenação
├── README.md              # Este arquivo
└── (outros arquivos de configuração)
```

## 🧪 Testando

Cada módulo pode ser testado independentemente:

```python
# Teste para fatores primos
assert fatores_primos(630) == [2, 3, 3, 5, 7]
assert fatores_primos(13) == [13]
assert fatores_primos(60) == [2, 2, 3, 5]

# Teste para palíndromos
assert eh_palindrome("Socorram-me, subi no ônibus em Marrocos!") == True
assert eh_palindrome("Olá mundo!") == False
assert eh_palindrome("arara") == True

# Teste para ordenação de palavras
assert ordenando_palavras('maçã LARANJA banana') == 'banana LARANJA maçã'
assert ordenando_palavras('zebra abacaxi gato') == 'abacaxi gato zebra'
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **Módulo `re`**: Para expressões regulares no verificador de palíndromos
- **Algoritmos**: Divisão sucessiva, manipulação de strings, ordenação

## 📚 Conceitos Aplicados

### No desafio de Fatores Primos:
- Algoritmos de fatoração
- Estruturas de repetição (`while`)
- Divisão inteira e resto
- Listas em Python

### No desafio de Palíndromos:
- Expressões regulares
- Manipulação de strings
- Limpeza e normalização de texto
- Comparação de strings

### No desafio de Ordenação:
- Métodos de string (`split`, `join`, `casefold`)
- Funções de ordenação (`sorted`)
- Parâmetros `key` para ordenação personalizada
- Preservação de estado original

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras

Para cada desafio, possíveis melhorias incluem:

### Fatores Primos:
- Otimização para números muito grandes
- Implementação do Crivo de Eratóstenes
- Suporte para números negativos

### Palíndromos:
- Normalização de caracteres Unicode
- Suporte a múltiplos idiomas
- Cache de resultados para melhor performance

### Ordenação de Palavras:
- Suporte a diferentes separadores
- Opção de ordenação ascendente/descendente
- Tratamento de stop words
