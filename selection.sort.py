# Declarando um array de números com 15 posições, não ordenados
array = [75, 23, 56, 12, 89, 4, 98, 32, 1, 47, 60, 15, 88, 19, 41]

print("Array original (não ordenado):")
print(array)

# Primeiro laço for para percorrer todo o array
for i in range(len(array)):
    # Variável para armazenar o índice do menor elemento encontrado
    min_idx = i
    
    # Segundo laço para buscar o menor elemento no restante do array
    for j in range(i+1, len(array)):
        # Condição para verificar se o valor na posição min_idx é maior que na posição j
        if array[min_idx] > array[j]:
            # Atualiza o índice do menor elemento
            min_idx = j
            
    # Troca dos valores do array utilizando desestruturação do Python (tuple unpacking)
    # Isso realiza a troca descrita nas instruções de forma segura sem perder o valor original
    array[i], array[min_idx] = array[min_idx], array[i]

print("\nArray ordenado de forma crescente pelo Selection Sort:")
print(array)
