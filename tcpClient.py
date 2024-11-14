import socket

def main() :
    # In client enter IP and Port to whom you want to connect
    target_host = "127.0.0.1"
    target_port = 1234         

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client : 

    # Connect the client
        client.connect((target_host, target_port))
        
        while True :
            msg = input("Enter 'exit' to exit the server or the message to the server : ")

            if msg.lower() == 'exit' :
                client.sendall(msg.encode('utf-8'))
                client.close()
                break


            # Send some data
            client.sendall(msg.encode('utf-8'))

            # Receive some data
            response = client.recv(4096)
            print(f"Recieved from Server : {response.decode('utf-8')}")


if __name__ == '__main__' :
    main()