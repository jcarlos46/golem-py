import os
from stat import S_ISDIR

def remote_isdir(sftp, path):
	try:
		return S_ISDIR(sftp.stat(path).st_mode)
	except IOError:
		return False

def isdir(file, sftp=None):
	if sftp:
		return remote_isdir(sftp, file)
	else:
		return os.path.isdir(file)

def mkdir(path, sftp=None):
	if sftp:
		if not isdir(path, sftp):
			sftp.mkdir(path)
	else:
		if not isdir(path):
			os.mkdir(path)