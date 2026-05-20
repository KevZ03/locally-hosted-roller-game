import os
from datetime import datetime
import socket
import json
from dotenv import load_dotenv

load_dotenv()

def extra():
    now = datetime.now()
    return f'{now.strftime("%I:%M %p")} [GAME SERVER] '

update_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def RelayDataToClient(data, command, info=None):
    print(extra(), f"SERVER RELAY RECEIVE: Command: {command}, Extra data: {info}, data: {data}")

    command = command.strip().lower()

    if command == 'update_join':
        name_list = []
        for player in data['players']: name_list.append(player['name'])
        for player in data['players']:
            ip, port = player['client_address']
            full_message = [command, name_list]
            full_message = json.dumps(full_message).encode()
            update_socket.sendto(full_message, (ip, port))

    elif command == 'update_leave':
        player_data = data[1]
        remove_player_name = data[0]
        print(data)
        for player in player_data['players']:
            ip, port = player['client_address']
            full_message = [command, remove_player_name]
            full_message = json.dumps(full_message).encode()
            update_socket.sendto(full_message, (ip, port))

    elif command == 'update_host_leave' or command == 'update_game_start':
        if command == 'update_game_start':
            server_name = info
            with open("admin_server_list.json") as server_data:
                server_json = json.load(server_data)

            for servers in server_json:
                if servers['server_name'] == server_name:
                    servers['server_status'] = 'In Game'
                    break

            with open('admin_server_list.json', 'w') as file:
                json.dump(server_json, file, indent=4)


        for player in data:
            ip, port = player['client_address']
            full_message = [command]
            full_message = json.dumps(full_message).encode()
            update_socket.sendto(full_message, (ip, port))

    elif command == 'update_game_roll_dice' or command == 'update_game_stay_dice':
        dice_amount, user_name, server_name = info.split('/')

        if command == 'update_game_roll_dice':
            with open("admin_server_list.json") as server_data:
                server_json = json.load(server_data)

            for servers in server_json:
                if servers['server_name'] == server_name:
                    for players in servers['players']:
                        if players['name'] == user_name:
                            players['rolls'] = dice_amount
                            break
                    break


            with open('admin_server_list.json', 'w') as file:
                json.dump(server_json, file, indent=4)


        for player in data:
            ip, port = player['client_address']
            full_message = [command]
            if command == 'update_game_roll_dice':
                full_message = [command, dice_amount]
            elif command == 'update_game_stay_dice':
                full_message = [command, dice_amount, user_name]
            print(extra(), f'DICE ROLL GENERATED or STAY {full_message}')
            full_message = json.dumps(full_message).encode()
            update_socket.sendto(full_message, (ip, port))

    elif command == 'request_highest_player_rolls':
        highest_roll_list = []
        for player in data:
            new_roll = [player['name'], player['rolls']]
            highest_roll_list.append(new_roll)

        for player in data:
            ip, port = player['client_address']
            full_message = [command, highest_roll_list]
            print(extra(), f'Highest Dice Roll per Person: {full_message}')
            full_message = json.dumps(full_message).encode()
            update_socket.sendto(full_message, (ip, port))







def find_server_lobby(name):
    with open("admin_server_list.json") as server_data:
        server_json = json.load(server_data)
    for servers in server_json:
        if servers['server_name'] == name:
            return servers['players']
        else:
            return None


def remove_segment(server_name):
    ListOfPlayers = []
    with open("admin_server_list.json") as server_data:
        server_json = json.load(server_data)

    for server in server_json:
        if server['server_name'] == server_name:
            ListOfPlayers = server['players']
            server_json.remove(server)
            break

    with open('admin_server_list.json', 'w') as file:
        json.dump(server_json, file, indent=4)

    return ListOfPlayers

def remove_player(leave_json_data, player_name):
    for server in leave_json_data:
        server['server_current_player'] -= 1

        for player in server['players']:
            if player['name'] == player_name:
                server['players'].remove(player)
                print(extra(), f'REMOVED PLAYER: {player["name"]} FROM: {server["server_name"]}')
                return server

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def listen_for_requests(view_key, create_key, join_key, leave_key, instruction_key, server_address):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_address, 12345))
    print(extra(), 'GAME SERVER IS RUNNING - LISTENING FOR USERS AND DISCOVERY')

    while True:
        data, client_address = server_socket.recvfrom(4096)
        print(extra(), "Received request from:", client_address, data.decode())
        request_key = data.decode()

        with open("admin_server_list.json") as server_data:
            server_json = json.load(server_data)

        if request_key == view_key:
            server_list = json.dumps(server_json).encode()
            server_socket.sendto(server_list, client_address)
        elif request_key == create_key:
            data, _ = server_socket.recvfrom(4096)
            json_data = json.loads(data.decode())
            print(extra(), "Received JSON data from client:", json_data)

            update_port = json_data[2]
            server_data = json_data[1]
            user_name = json_data[0]
            server_name = server_data['server_name']
            server_data['server_current_player'] += 1
            player_data = {
                "name": user_name,
                "client_address": (client_address[0], update_port),
                "balance": 500,
                "rolls": 0,
                "turn": 0
            }

            if any(server['server_name'] == server_name for server in server_json):
                response_message = f"{server_name} is already exist, Please Choose a Different Name"
            else:
                with open("admin_server_list.json", 'r') as f:
                    existing_data = json.load(f)
                    server_data['players'].append(player_data)
                    existing_data.append(server_data)

                with open("admin_server_list.json", 'w') as f:
                    json.dump(existing_data, f, indent=4)
                response_message = f"{server_name} Successfully been created!"

            server_socket.sendto(response_message.encode(), client_address)
        elif request_key == join_key:
            json_data, _ = server_socket.recvfrom(4096)
            data = json.loads(json_data.decode())
            target = data[0]
            user_name = data[1]
            player_data = {
                "name": user_name,
                "client_address": [],
                "balance": 500,
                "rolls": 0,
                "turn": None
            }

            update_port = data[2]  # Expecting update_port to be sent from client
            print(extra(), "Received target from client:", target)

            response_message = ['Empty']
            ServerCurrentData = None
            for servers in server_json:
                if str(servers['server_name']).strip().lower() in str(target.strip().lower()):
                    if servers['server_current_player'] < servers['server_size'] and servers['server_status'] == 'In Lobby':
                        print(extra(), "RESPONSE TRUE\n" + str(player_data))
                        response_message = ['true', servers]
                        player_data['client_address'] = (client_address[0], update_port)  # Include update port
                        player_count = int(len(servers['players']))
                        player_data['turn'] = player_count
                        servers['players'].append(player_data)
                        servers['server_current_player'] += 1

                        with open("admin_server_list.json", 'w') as f:
                            json.dump(server_json, f, indent=4)
                        ServerCurrentData = servers
                        RelayDataToClient(data=ServerCurrentData, command='update_join')

                        break
                    elif servers['server_current_player'] >= servers['server_size']:
                        res = f'{target}: Maximum Player Reached'
                        print(extra(), res)
                        response_message = ["false", res]
                        break
                    elif servers['server_status'] == 'In Game':
                        res = f'{target}: Server Game has Already Started, Unable to join.'
                        print(extra(), res)
                        response_message = ["false", res]
                        break

            request_response = json.dumps(response_message)
            server_socket.sendto(request_response.encode(), client_address)

        elif request_key == leave_key:
            user_name, _ = server_socket.recvfrom(4096)
            user_name = user_name.decode().split('/')
            print(extra(), user_name)
            if user_name[0] == 'server':
                ListOfPlayers = remove_segment(user_name[1])
                print(extra(), f'Removed Server: {user_name[1]} ')
                RelayDataToClient(data=ListOfPlayers, command='update_host_leave')
                server_socket.sendto("true".encode(), client_address)

            elif user_name[0] == 'user':
                with open("admin_server_list.json") as server_data:
                    json_data = json.load(server_data)
                PlayersInLobby = remove_player(json_data, user_name[1])
                updated_json_string = json.dumps(json_data, indent=4)
                with open("admin_server_list.json", "w") as server_data:
                    server_data.write(updated_json_string)
                print(extra(), f"Removed player: {user_name[1]}")
                try:
                    RelayDataToClient(data=[user_name[1], PlayersInLobby], command='update_leave')
                    server_socket.sendto("true".encode(), client_address)
                except TypeError:
                    server_socket.sendto("false".encode(), client_address)


        elif request_key == instruction_key:
            data, _ = server_socket.recvfrom(4096)
            if data.decode() == instruction_key:
                data, _ = server_socket.recvfrom(4096)
            print(extra(), f'INSTRUCTION REQUEST RECEIVE: {data.decode()}')
            try:
                instruction_data = data.decode().split(":", 2)
                RelayDataToClient(data=find_server_lobby(instruction_data[0]), command=instruction_data[1], info=instruction_data[2])
                print(extra(), 'Instruction passed 2 arguments')
            except IndexError:
                instruction_data = data.decode().split(":", 1)
                RelayDataToClient(data=find_server_lobby(instruction_data[0]), command=instruction_data[1])
                print(extra(), f'Instruction passed 1 arguments {IndexError}')
            except Exception as e:
                print(f" ERROR SERVER: An error occurred: {e}")

        elif request_key == "DISCOVER_SERVER_IP":
            server_socket.sendto(get_local_ip().encode(), client_address)



def ClearServer():
    with open('admin_server_list.json', 'w') as f:
        f.write('[]')

if __name__ == '__main__':
    ClearServer()
    view_key = os.getenv('SV_REQUEST_KEY')
    create_key = os.getenv('SV_CREATE_KEY')
    join_key = os.getenv('SV_JOIN_KEY')
    leave_key = os.getenv('SV_LEAVE_KEY')
    instruction_key = os.getenv('SV_INSTRUCTION_KEY')

    local_ip = get_local_ip()
    print(extra(), "Server IP address:", local_ip)
    listen_for_requests(view_key, create_key, join_key, leave_key, instruction_key, local_ip)
