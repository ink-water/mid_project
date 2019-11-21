from socket import *
from server_settings import *


class Server:
    """与客户端连接的服务器"""

    def __init__(self):
        self.sock_fd = socket()
        self.sock_fd.bind(server_address)
        self.sock_fd.listen(3)

    def main(self):
        pass


if __name__ == '__main__':
    server = Server()
    server.main()
