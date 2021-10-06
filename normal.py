import pyautogui
import socket
import time
import random
import json


def moveTo(a,b):
    pyautogui.moveTo(a,b)

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 12345))

server_socket.listen(1)

(client_socket, client_address) = server_socket.accept()

while True:
    client_bytes = client_socket.recv(1024)
    client_input = client_bytes.decode('utf-8')
    if not is_json(client_input):
        client_socket.send("Not a valid json".encode('utf-8'))
    else:
        client_input = json.loads(client_input)
        if client_input['type'] == 'TIME':
            client_socket.send(time.strftime("%c").encode('utf-8'))
        elif client_input['type'] == 'MOVE':
            moveTo(client_input['x'], client_input['y'])
            client_socket.send("ok".encode('utf-8'))
        elif client_input['type'] == 'RAND':
            client_socket.send(str(random.randrange(0, 11)).encode('utf-8'))
        elif client_input['type'] == 'NAME':
            client_socket.send("My master called me \"Arik\". Funny, ha?".encode('utf-8'))
        elif client_input['type'] == 'EXIT':
            client_socket.send("Exiting.".encode('utf-8'))
            break
        else:
            client_socket.send("Unknown command")

client_socket.close()
server_socket.close()



   