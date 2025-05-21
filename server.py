import socket

HOST = "127.0.0.1"
PORT = 54321

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Server starts listening on {HOST}: {PORT}")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print(f"[SERVER] Server stops listening on {HOST}: {PORT}")

        print(f"[SERVER] Server socket closing.")
        server.close()

if __name__ == "__main__":
    start_server()