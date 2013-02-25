import os
from utils import isdir

def remote_copy(sftp, file):
	data = ''
	if not isdir(file, sftp):
		data = sftp.open(file).read()
	return data

def local_copy(file):
	data = ''
	if os.path.isfile(file):
		data = open(file).read()
	return data

def copy(file='', sftp=None):
	if sftp:
		return remote_copy(sftp, file)
	else:
		return local_copy(file)

