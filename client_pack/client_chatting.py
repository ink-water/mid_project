"""不能使用标准输入,缺少的必要字面值以参数传递"""


class ClientChatting:
    """客户端聊天功能"""

    def __init__(self, name=None):
        self.name = name

    def renew_chat_record(self, friend_name):
        """
            显示当前用户与目标好友七天内的聊天记录
        :param friend_name:
        :return: "name content  name content  ..."记录之间两个空格，昵称与内容之间一个空格
        """
        pass

    def chat_with_friend(self, friend_name):
        """
            私聊，显示当前用户与目标好友七天内的聊天记录，存储聊天记录至数据库以及将聊天内容显示给目标用户
        :param friend_name: 私聊好友昵称
        :return:
        """
        pass

    def chat_in_society(self):
        """
            公会聊天，显示公会聊天数据库的所有内容，存储聊天记录，给每个公会成员显示
        :return: "name content"
        """
        pass

    def chat_in_world(self):
        """
            世界聊天，显示公会聊天数据库的所有内容，给每个玩家显示
        :return:
        """
        pass

    def system_info(self):
        """
            系统公告，显示每一个玩家
        :return:
        """
        pass

    def add_friend(self, uid=0, name=""):
        """
            根据用户id或者用户昵称申请添加好友
        :param uid:
        :param name:
        :return:
        """
        pass

    def enter_society(self, sid=0):
        """
             根据公会id申请加入公会
        :param sid:
        :return:
        """
        pass

    def create_society(self, name, img=None, sign=None):
        """
            建立公会，添加公会名称、公会头像和公会签名
        :param name: 公会名称
        :param img: 公会头像
        :param sign: 公会签名
        :return:
        """
        pass

    def quit_society(self):
        """
            退出公会
        :return:
        """
        pass
