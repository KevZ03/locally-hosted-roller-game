import socket
import json

extra = 'LOGIN SERVER:'


def receive(data):
    result = check_data(data)

    if result is True:
        print(extra, "Received data:", data)
        return 'true'
    else:
        return 'false'


def check_data(login):
    with open('admin_login_server_data.json', 'r') as file:
        data = json.load(file)

    print(f"Login State: {login['state']}, User: {login['user']}")

    if login['state'] == '0':
        # Login State
        for player in data['player']:
            if player['user'] == login['user']:
                if player['password'] == login['password']:
                    print(extra, f'User Login Successfully: {player["user"]}')
                    return True
    elif login['state'] == '1':
        for player in data['player']:
            # print(player['user'], login['user'])
            if login['user'] == player['user']:
                return "exist"
            else:
                add_player(login['user'], login['password'])
                return True

    return False


def add_player(name, password):
    with open('admin_login_server_data.json', 'r') as file:
        data = json.load(file)

    new_player = {
        "user": name,
        "password": password,
        "value": 500
    }

    data["player"].append(new_player)

    with open('admin_login_server_data.json', 'w') as file:
        json.dump(data, file, indent=2)


def get_local_ip():
    return socket.gethostbyname(socket.gethostname())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = socket.gethostbyname(socket.gethostname())
    server_socket.bind((server_address, 65535))

    print(f'LOGIN SERVER IS RUNNING - LISTENING FOR LOGIN: ADDRESS {server_address}')

    while True:
        message, client_address = server_socket.recvfrom(4096)
        print("Received request from:", client_address, message.decode())

        request_key = message.decode()

        if request_key == "DISCOVER_LOGIN_IP":
            server_socket.sendto(get_local_ip().encode(), client_address)

        elif request_key == "LOGIN":
            new_message, client_address = server_socket.recvfrom(4096)
            print(new_message.decode())
            try:
                data = json.loads(new_message.decode())
                response = receive(data)
                server_socket.sendto(response.encode(), client_address)
            except Exception as e:
                print(f"Error processing message: {e}")
                server_socket.sendto('false'.encode(), client_address)


if __name__ == '__main__':
    main()
