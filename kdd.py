import time

# --- Leitura do Arquivo loremipsum.txt ---
palavras = list()

# Lendo o arquivo original linha por linha utilizando a instrução 'with'
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # Separa a linha em palavras removendo espaços em branco
        palavras_linha = linha.strip().split()
        for palavra in palavras_linha:
            # Limpeza das pontuações comuns para isolar as palavras puras
            palavra_limpa = palavra.strip(",.?!:;()\"'")
            if palavra_limpa:
                palavras.append(palavra_limpa.lower()) # Padroniza em minúsculas

print(f"Total de palavras carregadas: {len(palavras)}")

# --- Ordenação ---
# Escolhemos o método nativo sort() por ser o mais eficiente (O(N log N) via Timsort)
inicio = time.perf_counter()
palavras.sort()
fim = time.perf_counter()

tempo_execucao = fim - inicio
print(f"Ordenação concluída pelo método nativo sort() em: {tempo_execucao:.8f} segundos")

# --- Gravação do Resultado ---
# Criando um novo arquivo txt para armazenar as palavras ordenadas
with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + "\n")

print("Arquivo 'palavras_ordenadas.txt' gerado com sucesso com as palavras ordenadas!")
