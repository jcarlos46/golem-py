import re
import os
import paramiko
from getpass import getpass

def info(path):
        user = re.search('(.*)@',path).group(1)
        host = re.search('@(.*):',path).group(1)
        port = re.search(':(\d+)\/',path).group(1)
        root = re.search(':\d+(\/.*)',path).group(1)
	root = os.path.abspath(root)

        return Info(user, host, port, root)

def sftpclient(path):
	info = info(path)
	password = getpass(info.host + "\'s password: ")

	t = paramiko.Transport((info.host,info.port))
	t.start_client()
	t.auth_password(info.user,password)

	sftp = t.open_session()
	sftp = paramiko.SFTPClient.from_transport(t)

	return sftp

class Info:
	def __init__(self, user, host, port, root):
		self.user = user
		self.host = host
		self.port = int(port)
		self.root = root