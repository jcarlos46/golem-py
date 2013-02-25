import os

def remote_paths(sftp, root, ignore=[]):
	paths = [root]
	try:
		for path in sftp.listdir(root):
			path = os.path.join(root, path)
			if not path in ignore:
				if remote_isdir(sftp, path):
					paths += remote_paths(sftp, path)
				else:
					paths.append(path)
	except IOError:
		pass
	return paths

def local_paths(root, ignore=[]):
	paths = [root]
	if os.path.exists(root):
		for path in os.listdir(root):
			path = os.path.join(root,path)
			if not path.decode('utf-8') in ignore:
				if os.path.isdir(path):
					paths += local_paths(path)
				else:
					paths.append(path)
	return paths

def paths(root, ignore = [], sftp=None):
	if sftp:
		return remote_paths(sftp, root, ignore)
	else:
		return local_paths(root, ignore)