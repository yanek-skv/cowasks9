from random import randint
import os
import sys
#sys.exit()

def cows(x,y):
    return os.system(f'bash cowbash.sh {x} {y}')

n=sum(1 for dict in open('dictionaryW', 'r'))  #число строк в словаре
while True:
    idx = randint(0, n-1)
    f = open('dictionaryW', 'r')
    fd = f.readlines()     #считывает все строки из файла
    dic = (eval(fd[idx]))   #приобразуем строку в словарь
    word = (list(dic.keys())[0])   #слово
    task = (list(dic.values())[0]) #определение
    cows("Ответти на вопрос:", task)
    lw = ['*' for x in range(len(word))]
    i = 3


    while True:
        if not i:
            print('Попыток больше нет')
            break
        elif not '*' in lw:
            cows('Поздравляем! Вы отгадали слово', word )
            #print(f'Поздравляем! Вы отгадали слово "{word}"')
            break
        print(*lw)
        char = input('Вводите по одной букве: ')
        if char in word:
            for k, v in enumerate(word):
                if v == char:
                    lw[k] = char
                    print ("да есть такая буква")
        elif char == "0":
            #break
            sys.exit()
        else:
            i -= 1
            print(f'Такой буквы нет. Осталось попыток: {i}')