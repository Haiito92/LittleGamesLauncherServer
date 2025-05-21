import socket
import threading

HOST = "127.0.0.1"
PORT = 54321


class LauncherServer:
    
    def __init__(self, host: str = "127.0.0.1", port: int = 54321):
        self.__host: str = host
        self.__port: int = port
        self.__server_socket: socket.socket = None
        self.__running = false

    def handle_client(self, conn: socket, addr: tuple[str, int]):
        print(f"[SERVER] Accepted client connection")
        conn.close()

    def start_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"[SERVER] Server starts listening on {HOST}: {PORT}")

        try:
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[SERVER] Active connections: {threading.active_count() - 1}")            
        except KeyboardInterrupt:
            print(f"[SERVER] Server stops listening on {HOST}: {PORT}")

            print(f"[SERVER] Server socket closing.")
            server.close()