def remote_paste(sftp, file, data):
	f = sftp.open(file, 'w')
	f.write(data)
	f.close()

def local_paste(file, data):
	f = open(file, 'w')
	f.write(data)
	f.close()

def paste(file, data, sftp=None):
	if sftp:
		remote_paste(sftp, file, data)
	else:
		local_paste(file, data)
