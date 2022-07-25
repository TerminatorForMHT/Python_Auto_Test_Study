#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 0:59
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT/-
# @File    : Test1.py
from CommonLib.TestStart import BaseCase

test_player = BaseCase('ServerTest', hostname='TencentCloud')
ret = test_player.conn.exec_command('ip a')
print(ret)