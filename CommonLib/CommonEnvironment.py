#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/13 0:19
# @Author  : WangChenjin
# @Github  : https://github.com/TerminatorForMHT
# @Software: PyCharm
# @File    : CommonEnvironment.py.py
import paramiko


class SSHConnection(object):
    def __init__(self, usr, passwd, host, port):
        self._host = host
        self._port = port
        self._username = usr
        self._password = passwd
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    def exec_command(self, command, is_retcode=False):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        out_data = stdout.read().decode('utf-8').strip()
        err_data = stderr.read().decode('utf-8').strip()
        returncode = stdout.channel.recv_exit_status()
        if is_retcode:
            return returncode
        if len(err_data):
            return err_data
        return out_data

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)
