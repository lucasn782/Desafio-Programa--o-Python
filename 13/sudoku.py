from itertools import product


def resolver_sudoku(sudoku):
    for(linha, coluna) in product(range(0, 9), repeat=2):
        if sudoku[linha][coluna] == 0:
            for num in range(1, 10):
                permitido = True
                for i in range(0, 9):
                    if num in(sudoku[i][coluna], sudoku[linha][i]):
                        permitido = False
                        break
                for(i, j) in product(range(0, 3), repeat=2):
                    if sudoku[linha - linha % 3 + i][coluna - coluna % 3 + j] == num:
                        permitido = False
                        break
                if permitido:
                    sudoku[linha][coluna] = num
                    if tentativa := resolver_sudoku(sudoku):
                        return tentativa
                    sudoku[linha][coluna] = 0
            return False
    return sudoku


def mostrar_sudoku(sudoku):
    sudoku = [['*' if num == 0 else num for num in linha] for linha in sudoku]
    print()
    for linha in range(0, 9):
        if((linha % 3 == 0) and (linha != 0)):
            print('-' * 33)
        for coluna in range(0, 9):
            if((coluna % 3 == 0) and (coluna != 0)):
                print(' | ', end='')
            print(f' {sudoku[linha][coluna]} ', end='')
        print()
    print()
    
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]