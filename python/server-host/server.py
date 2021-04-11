import socket			

def logger(*message):
    print("SERVER: ", message)

def messages():
    return [
        "Message 1 from Server"
    ]

def socket_connection():
    s = socket.socket()
    logger("Socket successfully created")

    port = 1313

    s.bind(('', port))
    logger("Socket binded to port ", port)

    s.listen(5)
    logger("Socket is listening")

    return s

def message_receiver(conn):
    logger("Received Message: ", conn.recv(1024))

def message_sender(conn):
    logger("Sending ACK to client")
    conn.send("Message received successfully".encode())

def connection_close(conn):
    logger("Server connection closed")
    conn.close()


def main():
    try:
        skt = socket_connection()

        while True:
            conn, addr = skt.accept()	
            logger("Got connection from", addr)

            message_receiver(conn)
            message_sender(conn)
            connection_close(conn)
        
    except Exception as e:
        connection_close(conn)
        logger("Something went wrong in Server", e)
    finally:
        logger("Server's finally")
        skt.close()

if __name__ == "__main__":
    main()
