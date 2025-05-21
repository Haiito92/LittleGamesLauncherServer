import socket

class LauncherServer:
    
    def __init__(self, host: str = "127.0.0.1", port: int = 54321):
        self.__host: str = host
        self.__port: int = port
        self.__server: socket.socket = None
        self.__running = False
        
    def handle_client(self, conn: socket, addr: tuple[str, int]):
        print(f"[SERVER] Accepted client connection")
        conn.close()

    def accept_clients(self):
        try:
            while True:
                conn, addr = self.__server.accept()
                self.handle_client(conn, addr)
        except KeyboardInterrupt:
            self.stop_server()

    def start_server(self):
        if(self.__running):
            return
        self.__running = True

        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((self.__host, self.__port))
        self.__server.listen()
        print(f"[SERVER] Server starts listening on {self.__host}: {self.__port}")

        self.accept_clients()

    def stop_server(self):
        if(not self.__running):
            return

        print(f"[SERVER] Server stops listening on {self.__host}: {self.__port}")

        print(f"[SERVER] Server socket closing.")
        self.__server.close()

        self.__running = False

if __name__ == "__main__":
    server:LauncherServer = LauncherServer()
    server.start_server()