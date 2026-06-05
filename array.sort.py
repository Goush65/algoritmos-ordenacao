import random

# --- PARTE 1: Array de Inteiros ---
print("=== ORDENAÇÃO DE INTEIROS ===")

# Criando um array (lista) de 15 posições com números inteiros aleatórios (de 1 a 100)
numeros = [random.randint(1, 100) for _ in range(15)]
print(f"Array original (não ordenado): {numeros}")

# Realizando a ordenação crescente utilizando o método sort()
numeros.sort()
print(f"Array ordenado de forma crescente: {numeros}")

# Realizando a ordenação decrescente utilizando o método sort(key=None, reverse=True)
numeros.sort(key=None, reverse=True)
print(f"Array ordenado de forma decrescente: {numeros}")

print("\n" + "="*40 + "\n")

# --- PARTE 2: Array de Strings ---
print("=== ORDENAÇÃO DE STRINGS ===")

# Criando um array (lista) de strings com os elementos solicitados (fora de ordem alfabética)
campos = ["nome", "dataNascimento", "cpf", "rg"]
print(f"Array original (não ordenado): {campos}")

# Realizando a ordenação crescente utilizando o método sort()
campos.sort()
print(f"Array ordenado de forma crescente: {campos}")

# Realizando a ordenação decrescente utilizando o método sort(key=None, reverse=True)
campos.sort(key=None, reverse=True)
print(f"Array ordenado de forma decrescente: {campos}")
