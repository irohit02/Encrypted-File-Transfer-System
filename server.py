import socket

def start_server(host="127.0.0.1", port=4456):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            with open('received_file.xml', 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print("XML file received and saved as 'received_file.xml'")

if __name__ == "__main__":
    start_server()