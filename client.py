import socket


def send_xml_file(file_path, host="127.0.0.1", port=4456):
    with open(file_path, 'r') as file:
        xml_data = file.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(xml_data.encode())  
        print("XML data sent successfully.")

if __name__ == "__main__":
    send_xml_file('output.xml')
