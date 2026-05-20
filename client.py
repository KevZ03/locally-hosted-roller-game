import socket, random
import sys
import os
import json
import threading
import random
from dotenv import load_dotenv
#from game import MainWindow  # Make sure the game module is properly imported

stop_update_thread = False


# Create an instance of DummyUI to pass to MainWindow

def generate_random_port():
    return random.randint(1024, 49151)

update_port = generate_random_port()

def discover_server_ip():
    cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    discovery_message = "DISCOVER_SERVER_IP"
    cs.sendto(discovery_message.encode(), ("<broadcast>", 12345))

    while True:
        try:
            cs.settimeout(5)
            cs_ip, _ = cs.recvfrom(4096)
            return cs_ip.decode()
        except socket.timeout:
            print("No server response. Enjoy Single Player")
            break


def generate_random_name_testing():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Fiona", "George", "Henry"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
    name = f'{random.choice(first_names)} {random.choice(last_names)}'
    return name

load_dotenv()

view_key = os.getenv('SV_REQUEST_KEY')
create_key = os.getenv('SV_CREATE_KEY')
join_key = os.getenv('SV_JOIN_KEY')
leave_key = os.getenv('SV_LEAVE_KEY')
instruction_key = os.getenv('SV_INSTRUCTION_KEY')
#os.environ["USER_NAME"] = generate_random_name_testing()

user_name = os.getenv('USER_NAME')

server_ip = discover_server_ip()

client_name = socket.gethostname()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = server_ip
port = 12345


def SendInstructionToServer(server_name, instruction, key=instruction_key, data=None):
    #Instruction is format like /close game
    client_socket.sendto(key.encode(), (server_address, port))
    if data is None:
        message = f'{server_name}:{instruction}'
        client_socket.sendto(message.encode(), (server_address, port))
    else:
        message = f'{server_name}:{instruction}:{data}'
        client_socket.sendto(message.encode(), (server_address, port))



def SendDataToServer(request_key, json_data=None):
    if json_data:
        client_socket.sendto(request_key.encode(), (server_address, port))
        request_bytes = json.dumps(json_data).encode()
        client_socket.sendto(request_bytes, (server_address, port))
    else:
        client_socket.sendto(request_key.encode(), (server_address, port))



def RequestLeaveServer(extra, key=leave_key):
    client_socket.sendto(key.encode(), (server_address, port))
    client_socket.sendto(extra.encode(), (server_address, port))
    server_response, _ = client_socket.recvfrom(4096)
    return server_response.decode().strip().lower() == 'true'

def RequestJoinServer(key=join_key, target=''):
    join_request_key = key
    client_socket.sendto(join_request_key.encode(), (server_address, port))



    json_data = [target, user_name, update_port]
    request_bytes = json.dumps(json_data).encode()
    client_socket.sendto(request_bytes, (server_address, port))

    server_response, _ = client_socket.recvfrom(4096)
    response = json.loads(server_response.decode())
    print("Server response after sending JSON data:", response)

    if response[0].strip().lower() == "true":
        return True, response[1]
    elif response[0].strip().lower() == "false":
        return False
    else:
        return "Empty"

def RequestCreateServer(usr_name, server_name, size=4, key=create_key):
    create_request_key = key
    client_socket.sendto(create_request_key.encode(), (server_address, port))
    server_status = "In Lobby"

    server_data = {
        "server_name": f'{str(server_name)}',
        "server_status": server_status,
        "server_size": int(size),
        "server_current_player": 0,
        "server_current_round": 1,
        "players": []
    }

    request_data = [usr_name, server_data, update_port]
    request_bytes = json.dumps(request_data).encode()
    client_socket.sendto(request_bytes, (server_address, port))

    server_response, _ = client_socket.recvfrom(4096)
    print("Server response after creating server:", server_response.decode())
    return True

def GetAvailableServers(key=view_key):
    client_socket.sendto(key.encode(), (server_address, port))
    server_response, _ = client_socket.recvfrom(4096)
    server = json.loads(server_response.decode())
    return server


from PySide2.QtCore import QObject

class Client(QObject):
    def __init__(self, game_window):
        super().__init__()
        self.game_window = game_window
        self.game_window.worker.update_signal.connect(self.update_game)

    def update_game(self, data):
        # Call the update_game function in the game window
        self.game_window.worker.update_game(data)