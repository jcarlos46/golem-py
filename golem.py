import json
import os
import sys
import shutil
import time
import zipfile

source = sys.argv[1]
zipname = time.strftime("%Y%m%d-%H%M%S") + ".zip"
config = os.path.join(source,"config.json")

if os.path.exists(config):
	f = open(config)
	f = json.load(f)
	if 'Destination' in f.keys():
		dest = f['Destination']
	else:
		dest = sys.argv[2]
else:
	dest = sys.argv[2]

def ignoreList(suffix): #monting list of ignored files
	ignore = [config]
	if os.path.exists(config):
		f = open(config)
		for i in json.load(f)['Ignore']:
			ignore.append(os.path.join(suffix,i))
		f.close()
	return ignore

ignore = ignoreList(dest)
paths = []
if os.path.exists(dest): #zipping destination files
	zip = zipfile.ZipFile(zipname, "w")
	for root, dirs, files in os.walk(dest):
		if root not in ignore:
			for file in files:
				if os.path.join(dest,file) not in ignore:
					zip.write(os.path.join(root, file))

	zip.close()
	shutil.rmtree(dest) #removing destination files

ignore = ignoreList(source)
if os.path.exists(source): #copying source files to destination
	for root, dirs, files in os.walk(source):
		if root not in ignore:
			os.mkdir(root.replace(source,dest + os.sep))
			for file in files:
				if os.path.join(source,file) not in ignore:
					shutil.copy(os.path.join(source,file),os.path.join(dest,file))
