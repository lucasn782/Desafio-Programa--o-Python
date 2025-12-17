# Fatores Primos

## Descrição
Este projeto contém uma função Python para encontrar todos os fatores primos de um número inteiro. Fatores primos são os números primos que, quando multiplicados, resultam no número original.

## Funcionalidade
A função `fatores_primos(numero)` recebe um número inteiro como entrada e retorna uma lista contendo todos os seus fatores primos em ordem crescente.

## Algoritmo
O algoritmo funciona da seguinte maneira:
1. Inicia com o menor número primo (2)
2. Divide o número pelo divisor atual enquanto a divisão for exata (resto = 0)
3. Quando a divisão não for mais exata, incrementa o divisor
4. Repete o processo até que o número se torne 1
5. Retorna a lista de fatores primos encontrados

## Código
```python
def fatores_primos(numero):
    fatores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return fatores
```

## Exemplos de Uso

### Exemplo 1: Número composto
```python
>>> fatores_primos(630)
[2, 3, 3, 5, 7]
```
Verificação: `2 × 3 × 3 × 5 × 7 = 630`

### Exemplo 2: Número primo
```python
>>> fatores_primos(13)
[13]
```
Verificação: `13 = 13`

### Exemplo 3: Outro número composto
```python
>>> fatores_primos(60)
[2, 2, 3, 5]
```
Verificação: `2 × 2 × 3 × 5 = 60`

## Como Usar
1. Salve o código em um arquivo Python (ex: `fatores_primos.py`)
2. Importe a função no seu código:
   ```python
   from fatores_primos import fatores_primos
   ```
3. Chame a função com um número inteiro:
   ```python
   resultado = fatores_primos(630)
   print(resultado)
   ```

## Requisitos
- Python 3.x

## Aplicações
- Matemática computacional
- Criptografia básica (entendimento de fatoração)
- Teoria dos números
- Problemas de divisibilidade

## Observações
- Para números primos, a função retorna uma lista contendo apenas o próprio número
- A ordem dos fatores na lista é crescente
- Fatores repetidos aparecem múltiplas vezes na lista (ex: para 12, retorna [2, 2, 3])
- O algoritmo é eficiente para números de tamanho moderado

## Limitações
- Para números muito grandes (como os usados em criptografia moderna), algoritmos mais sofisticados seriam necessários
- O algoritmo tem complexidade O(n) no pior caso (quando o número é primo)