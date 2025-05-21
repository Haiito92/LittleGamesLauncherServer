import socket
import threading

HOST = "127.0.0.1"
PORT = 54321

def handle_client(conn: socket, addr: tuple[str, int]):
    print(f"[SERVER] Accepted client connection")
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Server starts listening on {HOST}: {PORT}")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[SERVER] Active connections: {threading.active_count() - 1}")            
    except KeyboardInterrupt:
        print(f"[SERVER] Server stops listening on {HOST}: {PORT}")

        print(f"[SERVER] Server socket closing.")
        server.close()

if __name__ == "__main__":
    start_server()