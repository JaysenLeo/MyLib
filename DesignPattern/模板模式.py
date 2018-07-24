# -*- coding: utf-8 -*-


class Register(object):
    """用户注册接口"""

    def register(self):
        pass

    def login(self):
        pass

    def auth(self):
        self.register()
        self.login()


class RegisterByMail(Register):
    """邮箱注册"""

    def register(self):
        print("---用邮箱注册-----")

    def login(self):
        print("----用邮箱登录-----")


class RegisterByPhone(Register):
    """手机号注册"""

    def register(self):
        print("---用手机号注册-----")

    def login(self):
        print("----用手机号登录-----")


if __name__ == "__main__":

    register1 = RegisterByMail()
    register1.auth()

    register2 = RegisterByPhone()
    register2.auth()