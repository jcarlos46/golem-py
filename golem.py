import os
import sys
import zipfile
import shutil
import time
import json

source = sys.argv[1]
dest = sys.argv[2]
config = os.path.join(source,"config.json")
zipname = time.strftime("%Y%m%d - %H %M %S") + ".zip"

if os.path.exists(config):
  f = open(config)
	ignore = json.load(f)['Ignore']
	f.close()

if os.path.exists(dest):
	zip = zipfile.ZipFile(zipname, "w")
	for root, dirs, files in os.walk(dest):
		if root not in ignore:
			for file in files:
				if file not in ignore:
					zip.write(os.path.join(root, file))

	shutil.rmtree(dest)

shutil.copytree(source, dest)
