#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 0:37
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT/-
# @Software: PyCharm
# @File    : TestStart.py
import json

from CommonLib.CommonEnvironment import SSHConnection


class BaseCase():
    def __init__(self, type, **otheargs):
        """
        测试框架初始化函数
        :param type: 区分测试类型，有ServerTest，WebTest和AppTest三种
        :param otheargs: 根据不同测试类型输入所需参数
        """
        if type == 'ServerTest':
            self.env_name = otheargs.get('env_name')
            # \TestConfig\EnvInfo.json为你的服务器配置文件
            self.read = open('..\TestConfig\EnvInfo.json', 'r')
            self.info = json.load(self.read)
            self.read.close()
            self.hostinfo = None
            self.hostname = otheargs.get('hostname')
            for info in self.info:
                if self.hostname == info.get('hostname'):
                    self.hostinfo = info
                    break
            if self.hostinfo == None:
                print('环境信息不存在')
                assert False
            self.host = self.hostinfo.get('host')
            self.port = self.hostinfo.get('port')
            self.user = self.hostinfo.get('user')
            self.passwd = self.hostinfo.get('passwd')
            self._transport = None
            self._sftp = None
            self._client = None
            self.serverinit()

        elif type == 'Web':
            """
            Web测试初始化
            """
            pass

        else:
            """
            App测试初始化
            """
            pass

    def serverinit(self):
        self.conn = SSHConnection(self.user, self.passwd, self.host, self.port)
        return self.conn
