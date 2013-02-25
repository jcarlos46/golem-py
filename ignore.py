import json
import os

def remote_ignore(sftp, file):
	path = file.replace("config.json", "")
	try:
		if sftp.stat(file):
			f = sftp.open(file)
			j = json.loads(f.read().decode('utf-8'))
			i = j['Ignore']
			f.close()
	except:
		i = []
	a = []
	for v in i:
		a.append(os.path.join(path,v))
	return a

def local_ignore(file):
	path = file.replace("config.json", "")
	if os.path.exists(file):
		f = open(file).read()
		i = json.loads(f)['Ignore']
	else:
		i = []
	a = []
	for v in i:
		a.append(os.path.join(path,v))
	return a

def ignore(file, sftp=None):
	if sftp:
		return remote_ignore(sftp, file)
	else:
		return local_ignore(file)