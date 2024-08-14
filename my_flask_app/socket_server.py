import socket
import json

# JSON 데이터를 저장할 파일 이름
JSON_FILE = 'received_data.json'

def start_socket_server(host='0.0.0.0', port=7000, json_file=JSON_FILE):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Socket server started on {host}:{port}")
    except OSError as e:
        print(f"Error: {e}")
        return

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            with open(json_file, mode='a') as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    
                    # JSON 데이터 디코딩
                    decoded_data = data.decode('utf-8')
                    json_data = json.loads(decoded_data)
                    print(f"Received data: {json_data}")
                    
                    # JSON 파일에 데이터 추가
                    json.dump(json_data, file)
                    file.write('\n')  # 각 JSON 객체를 새 줄에 기록

        finally:
            client_socket.close()

if __name__ == '__main__':
    # 소켓 서버 실행
    start_socket_server()
