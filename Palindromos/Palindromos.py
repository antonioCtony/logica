import re
from collections import deque

def main ():

    palavra = input("Escreva algo: ");
    limpar_palavras = re.sub(r'[^a-z0-9]', '', palavra.lower());
    
    palavras_deque = deque(limpar_palavras)

    palindromo = True

    while len(palavras_deque)>1:
        if palavras_deque.popleft() != palavras_deque.pop():
            palindromo = False
        break

    if palindromo:
        print("Palindromo")
    else:
        print("Não Palindromo")




main()