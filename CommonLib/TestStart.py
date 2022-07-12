#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 0:37
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT/-
# @Software: PyCharm
# @File    : TestStart.py
import paramiko
import pytest

from CommonLib.CommonEnvironment import SSHConnection
from TestConfig.ConnectConfig import *


class BaseCase():
    def __init__(self, type, **otheargs):
        if type == 'ServerTest':
            self.config = Config()
            self.hostname = otheargs.get('hostname')
            for info in self.config.HostInfo:
                if info.get('hostname') == self.hostname:
                    self.hostinfo = info
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
