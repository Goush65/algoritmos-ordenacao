def bubbleSort(array):
    # Primeiro laço para iterar por todos os elementos do array
    for i in range(len(array)):
        # Segundo laço para comparar os elementos adjacentes
        # A cada passada, o maior elemento restante é colocado em sua posição final
        for j in range(0, len(array) - i - 1):
            # Condição para verificar se o elemento atual é maior que o próximo
            if array[j] > array[j+1]:
                # Troca os elementos de posição utilizando uma variável temporária
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

# Declarando um array de números com 15 posições, não ordenados
numeros = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45, 3, 50, 15, 29, 42]

print("Array original (não ordenado):")
print(numeros)

# Aplicando o método bubbleSort para ordenar o array
bubbleSort(numeros)

print("\nArray ordenado de forma crescente pelo Bubble Sort:")
print(numeros)
