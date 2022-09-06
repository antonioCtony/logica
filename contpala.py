"""You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
 return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""

def main():
    palavra = input("Escreva algo: ");
   
    middle_char = palavra[int(len(palavra)/2-1)]
    middle_char1 = palavra[int(len(palavra)/2)] 
    
    if len(palavra) % 2 == 0:
        middle_chars = middle_char + middle_char1
        print (middle_chars)
    else:
        middle_chars = palavra[int(len(palavra)/2)] 
        print( middle_chars)
main()

