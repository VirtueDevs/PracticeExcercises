import random


def guessTheNumber(x): #método para adivinar un número aleatorio
    random_number=random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivina el numero entre 1 y {x}: '))
        if guess < random_number:
            print("Lo sentimos, el número es muy bajo. Intentalo de nuevo")
        elif guess > random_number:
            print("Lo sentimos, el número es muy alto. Intentalo de nuevo")
        
    print(f"Felicidades, haz adivinado!  El número es {random_number}!")


def computer_guess(x): #método para que el computador adivine el número
    bajo=1
    alto=x
    comentario=''
    while comentario !='c':
        if bajo != alto:
            guess = random.randint(bajo, alto)
        else:
            guess = bajo #Podría ser alto porque bajo = alto
        comentario = input(f'Es {guess} muy alto (A), muy bajo (B), o correcto (C)?').lower()
        if comentario == 'a':
            alto=guess-1
        elif comentario =='b':
            bajo=guess+1

    print("La máquina ha adivinado de manera correcta")

computer_guess(20)

guessTheNumber(100)