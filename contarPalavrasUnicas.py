import re



contadorPalavra = input("Escreva algo: ")
contarBaixo =  re.sub(r'^\w\s', '', contadorPalavra.lower()) #Remove pontuações e o que estava maiusculo se torna minusculo

palavras = contarBaixo.split()

palavaras_unicas = set(palavras)

print(f"Palavras únicas: {palavaras_unicas}")
print(f"Número de palavras únicas: {len(palavaras_unicas)}")
