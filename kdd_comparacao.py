import time

# --- Implementação dos Algoritmos de Ordenação ---

def bubbleSort(array):
    arr = array.copy() # Copia para não alterar a lista original nos testes
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selectionSort(array):
    arr = array.copy() # Copia para não alterar a lista original nos testes
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- Leitura do Arquivo loremipsum.txt ---

palavras = list()

# Lendo o arquivo linha por linha com a instrução 'with'
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # Separa a linha em palavras (removendo quebras de linha e espaços extras)
        palavras_linha = linha.strip().split()
        for palavra in palavras_linha:
            # Limpeza básica: remove pontuações comuns para isolar as palavras
            palavra_limpa = palavra.strip(",.?!:;()\"'")
            if palavra_limpa: # Adiciona se a palavra não estiver vazia
                palavras.append(palavra_limpa.lower()) # Convertendo para minúsculas para padronizar

print(f"Total de palavras carregadas para ordenação: {len(palavras)}\n")
print("=== INICIANDO MEDIÇÃO DE PERFORMANCE ===")

# --- 1. Teste do Bubble Sort ---
inicio = time.perf_counter()
bubbleSort(palavras)
fim = time.perf_counter()
tempo_bubble = fim - inicio
print(f"Tempo de execução (Bubble Sort): {tempo_bubble:.8f} segundos")

# --- 2. Teste do Selection Sort ---
inicio = time.perf_counter()
selectionSort(palavras)
fim = time.perf_counter()
tempo_selection = fim - inicio
print(f"Tempo de execução (Selection Sort): {tempo_selection:.8f} segundos")

# --- 3. Teste do Método Nativo sort() ---
inicio = time.perf_counter()
palavras_copia = palavras.copy()
palavras_copia.sort()
fim = time.perf_counter()
tempo_native = fim - inicio
print(f"Tempo de execução (Método Nativo sort): {tempo_native:.8f} segundos")

print("\n=== COMPARATIVO FINAL ===")
print(f"1º Lugar (Mais Rápido): Método Nativo sort() -> {tempo_native:.8f}s")
print(f"2º Lugar: Selection Sort -> {tempo_selection:.8f}s")
print(f"3º Lugar: Bubble Sort -> {tempo_bubble:.8f}s")
