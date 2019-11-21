from socket import *
from server_settings import *


class ServerDatabase:
    """数据库服务器，将客户端的聊天记录存入指定数据库"""

    def __init__(self):
        self.sock_fd = socket()
        self.sock_fd.bind(server_address)
        self.sock_fd.listen(3)

    def main(self):
        pass


if __name__ == '__main__':
    server = ServerDatabase()
    server.main()
