# 1. Abrindo o arquivo usando a função open() tradicional
# Usamos encoding="utf-8" para garantir a leitura correta de caracteres especiais e acentos
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# 2. Imprimindo todo o conteúdo do arquivo
print("=== CONTEÚDO COMPLETO DO ARQUIVO ===")
conteudo_completo = arquivo.read()
print(conteudo_completo)
print("="*40 + "\n")

# Reposicionando o cursor para o início do arquivo para fazer novas leituras
arquivo.seek(0)

# 3. Imprimindo apenas a primeira linha do arquivo
print("=== APENAS A PRIMEIRA LINHA ===")
primeira_linha = arquivo.readline()
print(primeira_linha.strip()) # strip() remove quebras de linha adicionais
print("="*40 + "\n")

# Reposicionando o cursor para o início do arquivo novamente
arquivo.seek(0)

# 4. Imprimindo apenas os 3 primeiros caracteres do arquivo
print("=== APENAS OS 3 PRIMEIROS CARACTERES ===")
tres_caracteres = arquivo.read(3)
print(tres_caracteres)
print("="*40 + "\n")

# Fechando o arquivo aberto manualmente
arquivo.close()

# 5. Utilizando a instrução "with" para abrir, ler e imprimir o arquivo
print("=== LEITURA UTILIZANDO A INSTRUÇÃO 'WITH' ===")
with open("loremipsum.txt", "r", encoding="utf-8") as arquivo_with:
    conteudo_with = arquivo_with.read()
    print(conteudo_with)
print("="*40)
