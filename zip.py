import os
import zipfile

def local_zip(root, paths, zipname):
	if os.path.exists(root):
		zip = zipfile.ZipFile(zipname, 'w')
		for file in paths:
			if os.path.isfile(file):
				zip.write(file)
		zip.close()

def remote_zip(sftp, root, paths, zipname):
	if remote_isdir(sftp, root):
		zip = zipfile.ZipFile(zipname, 'w')
		os.mkdir('.tmp')
		os.chdir('.tmp')
		for file in paths:
			if not remote_isdir(sftp, file):
				data = remote_copy(sftp, file)
				f = open(file.replace(root + os.sep, ''), 'w')
				f.write(data)
				f.close()
				zip.write(f.name)
				os.remove(f.name)
		zip.close()
		os.chdir('..')
		os.rmdir('.tmp')

def zip(root, paths, zipname, sftp=None):
	if sftp:
		remote_zip(sftp, root, paths, zipname)
	else:
		local_zip(root, paths, zipname)