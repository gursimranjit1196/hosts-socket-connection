# Import socket module
import socket
import time
import json
import datetime

def logger(*message):
    print("CLIENT: ", message)

def messages():
    return [
        "Message 1 from Client",
        "Message 2 from Client",
        "Message 3 from Client",
    ]

def get_messages():
    return {
        "messages": messages(),
        "index": 0
    }

def socket_connection():
    s = socket.socket()
    logger("Socket successfully created")

    port = 1313

    logger("Connecting with server on Port", port)
    s.connect(('server_host', port))

    s.send("Hi Server".encode())

    return s

def message_sender(skt, data):
    if data["index"] < len(data["messages"]):
        msg = data["messages"][data["index"]]
        logger("Sending Message: ", msg)
        skt.send(msg.encode())
        data["index"] += 1
    else:
        raise "All messages sent."

def message_receiver(skt, data):
    logger("Received Message: ", skt.recv(1024))

def socket_close(skt):
    logger("Closing connection from Client")
    skt.close()

def main():
    try:
        data = get_messages()
        skt = socket_connection()
        message_receiver(skt, data)
        message_sender(skt, data)
    except Exception as e:
        logger("Something went wrong in Client", e)
    finally:
        logger("Client's finally")
        skt.close()

if __name__ == "__main__":
    main()
