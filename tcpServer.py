import socket

def main() :

    hostIP = '127.0.0.1' # Host IP
    hostPort = 1234      # Host port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server :
        
        server.bind((hostIP, hostPort))
        server.listen()
        print(f"[+] Server Listening on {hostIP} : {hostPort}....")

        while True :
            # Accept incoming connection
            client_socket, client_addr = server.accept()
            with client_socket :
                print(f"[+] Accpeted connection from {client_addr}")

                # Recieve data from the client
                data = client_socket.recv(4096)

                if data :

                    msg = data.decode('utf-8')
                    print(f"Recieved : {msg}")

                    if msg == 'exit' :
                        break

        print("Server closed")
        server.close()



if __name__ == '__main__' :
    main()