# 1. Abrindo o arquivo 'texto.txt' em modo de escrita ('w')
# Se o arquivo não existir, o Python o criará automaticamente.
# Usamos encoding="utf-8" para garantir suporte a acentos e caracteres especiais.
arquivo = open("texto.txt", "w", encoding="utf-8")

# 2. Criando uma lista vazia chamada 'texto' utilizando a sintaxe solicitada
texto = list()

# 3. Utilizando o método 'append' para adicionar frases à lista
# Adicionamos a quebra de linha '\n' no final de cada frase para que fiquem em linhas separadas
texto.append("Esta é a primeira frase gravada no arquivo.\n")
texto.append("O método writelines() é ideal para salvar uma lista de strings.\n")
texto.append("Microatividade 5 de manipulação de arquivos concluída com sucesso!\n")

# 4. Escrevendo o conteúdo da lista no arquivo
arquivo.writelines(texto)

# 5. Fechando o arquivo para liberar os recursos do sistema operacional
arquivo.close()

print("Arquivo 'texto.txt' gerado e gravado com sucesso na pasta do projeto!")
