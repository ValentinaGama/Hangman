
import os
import random 

def select(words):
    return random.choice(words)

def guess(word,guessed,count):
    
    word=word
    guessed=guessed
    count+=1
    print("Adivina la palabra!!")
    print("va en el intento numero: " +str(count))
    letter=input("ingrese una letra: ")
    assert len(letter)==1, 'Ingresa solo una letra'

    os.system('clear')

    for h in range(len(word)):
        if letter==word[h]:
            guessed[h] = letter
    print(guessed)
    string=""
    string = (string.join(guessed))

    if string != word and count<7:
        guess(word,guessed,count)
    elif count>=7:
        print("Has llegado al  máximo de intentos")
    else:
        print("Has adivinado la palabra!")

def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f: 
        for line in f:
            words.append(line.strip('\n'))
    # print(words)
    return words


if __name__ == '__main__':
    count = 0
    words=read()
    wordt = select(words)
    wordsw=wordt.maketrans('áéíóú', 'aeiou')
    word = wordt.translate(wordsw)
    # print(word)
    guessed = ["-" for i in range(len(word))]
    print(str(guessed))
    guess(word,guessed,count)