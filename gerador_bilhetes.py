import itertools
import random

# Lista completa dos 56 bilhetes base
bilhetes_base = [
    [2, 8, 19, 30, 41, 49],
    [4, 10, 5, 32, 47, 45],
    [6, 12, 9, 34, 43, 50],
    [14, 20, 7, 36, 30, 48],
    [16, 22, 11, 38, 41, 49],
    [18, 24, 13, 40, 47, 50],
    [1, 3, 19, 26, 42, 44],
    [5, 7, 30, 28, 46, 48],
    [9, 15, 41, 29, 37, 49],
    [10, 17, 47, 31, 35, 50],
    [12, 19, 21, 33, 39, 44],
    [14, 23, 30, 27, 45, 50],
    [16, 25, 41, 35, 43, 48],
    [18, 19, 30, 37, 42, 49],
    [20, 21, 47, 29, 36, 50],
    [22, 24, 41, 31, 34, 48],
    [1, 5, 19, 38, 44, 47],
    [3, 7, 30, 40, 45, 49],
    [9, 13, 41, 26, 32, 50],
    [11, 15, 47, 28, 37, 48],
    [17, 19, 30, 33, 42, 49],
    [2, 6, 41, 35, 43, 50],
    [4, 8, 47, 29, 36, 48],
    [10, 12, 19, 31, 34, 49],
    [14, 16, 30, 27, 45, 50],
    [18, 20, 41, 37, 42, 48],
    [22, 24, 47, 39, 42, 49],
    [1, 3, 19, 28, 46, 50],
    [5, 7, 30, 33, 43, 48],
    [9, 11, 41, 35, 44, 49],
    [13, 15, 47, 31, 36, 50],
    [17, 19, 30, 34, 45, 48],
    [21, 23, 41, 37, 42, 49],
    [25, 2, 47, 29, 38, 50],
    [4, 6, 19, 26, 43, 48],
    [8, 10, 30, 32, 44, 49],
    [12, 14, 41, 35, 46, 50],
    [16, 18, 47, 27, 39, 48],
    [20, 22, 19, 31, 42, 49],
    [24, 1, 30, 33, 45, 50],
    [3, 5, 41, 37, 44, 48],
    [7, 9, 47, 29, 36, 49],
    [11, 13, 19, 34, 43, 50],
    [15, 17, 30, 38, 42, 48],
    [21, 23, 41, 35, 46, 49],
    [25, 2, 47, 31, 44, 50],
    [4, 6, 19, 27, 45, 48],
    [8, 10, 30, 29, 43, 49],
    [12, 14, 41, 37, 46, 50],
    [16, 18, 47, 33, 42, 48],
    [20, 22, 19, 35, 44, 49],
    [24, 1, 30, 36, 45, 50],
    [3, 5, 41, 38, 43, 48],
    [7, 9, 47, 34, 42, 49],
    [11, 13, 19, 31, 46, 50],
    [15, 17, 30, 39, 44, 48]
]

def dividir_em_duques(bilhete):
    """Divide um bilhete de 6 números em 3 duques."""
    return [bilhete[i:i+2] for i in range(0, 6, 2)]

def gerar_1400_bilhetes(bilhetes_base):
    duques = [dividir_em_duques(bilhete) for bilhete in bilhetes_base]
    todos_duques = [duque for sublist in duques for duque in sublist]
    
    bilhetes_gerados = []
    while len(bilhetes_gerados) < 1400:
        # Escolhe 3 duques aleatórios de bilhetes base diferentes
        duques_selecionados = random.sample(todos_duques, 3)
        novo_bilhete = list(set(num for duque in duques_selecionados for num in duque))
        
        # Verifica se tem 6 números únicos e balanceamento
        if len(novo_bilhete) == 6 and balanceado(novo_bilhete):
            bilhetes_gerados.append(sorted(novo_bilhete))
    
    return list(bilhetes_gerados)

def balanceado(bilhete):
    """Verifica se o bilhete tem 3 pares/ímpares e 3 baixos/altos."""
    pares = sum(1 for num in bilhete if num % 2 == 0)
    baixos = sum(1 for num in bilhete if num <= 25)
    return pares == 3 and baixos == 3

# Gera os 1.400 bilhetes
bilhetes_finais = gerar_1400_bilhetes(bilhetes_base)

# Salva em um arquivo .txt
with open("bilhetes_dupla_sena.txt", "w") as file:
    for bilhete in bilhetes_finais:
        file.write(" ".join(map(str, bilhete)) + "\n")
