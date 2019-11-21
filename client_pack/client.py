from socket import *
from pro_wzq.client_pack.client_chatting import ClientChatting
from pro_wzq.client_pack.client_chess import ClientChess
from pro_wzq.client_pack.client_settings import ClientSettings


class Client:
    """实现客户端基本的登录注册功能"""

    def __init__(self):
        self.settings = ClientSettings()

        # 该客户端的昵称
        self.name = None

        # 客户端的棋盘和聊天对象
        self.chat = None
        self.chess = None

        # 创建套接字
        self.sock_fd = socket()
        self.sock_fd.connect(self.settings.server_address)

    def name_is_legal(self, name):
        """
            验证昵称是否含有非法字符,即昵称中不允许含有空格
        :param name:
        :return: bool
        """
        pass

    def verify_name(self, name):
        """
            验证注册用户是否重名
        :param name:
        :return: bool
        """
        pass

    def password_is_legal(self, password):
        """
            验证密码是否合法,不允许密码中含有空格
        :param password:
        :return:
        """
        pass

    def same_password(self, password, password_):
        """
            保证前后密码输入相同
        :param password:
        :param password_:
        :return:
        """

    def register(self, name, password: str):
        """
            验证昵称之后、注册、注册后返回一级界面
        :param name:
        :param password:
        :return:
        """
        self.name = name
        pass

    def login(self, name, password):
        """
            登录检测
        :param name:
        :param password:
        :return:
        """
        self.name = name
        self.chat = ClientChatting(self.name)
        pass

    def protect_password(self, password):
        """
            给密码加密，登录时注册时使用
        :param password:
        :return:
        """
        # self.settings.salt 加盐字段
        pass

    def quit_game(self):
        """
            游戏结束的处理,清空公会、世界、系统聊天记录相关数据库,删除私聊数据库中超过七天的聊天记录
        :return:
        """
        pass

    def run_game(self):
        """
            使用多进程，1个进程负责处理下棋，1个负责聊天的收发
            处理下棋的进程中，使用多线程处理下棋、悔棋、和棋、认输功能
            在负责聊天收发的进程中使用多线程循环收发系统、世界、公会、私聊记录
        :return:
        """
        pass


if __name__ == '__main__':
    client = Client()
    client.run_game()
