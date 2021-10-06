# import all the required modules
import socket
import threading

nickname = input("Choose your nickname: ")

PORT = 9999
SERVER = "localhost"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(ADDRESS)

print(client)

def receive():
    while True:                                                
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:                                                 
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                
        message = '{}: {}'.format(nickname, input('Your message:'))
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                  
write_thread.start()