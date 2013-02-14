import os, json, shutil, utils

def copy(src,dst):
	if os.path.exists(dst): shutil.rmtree(dst) #removing dstination files
	ignore = utils.ignore(src,src)
	if os.path.exists(src): #copying source files to dstination
		for root, dirs, files in os.walk(src):
			if root not in ignore:
				print("Copying " + src + "...")
				os.mkdir(root.replace(src,dst + os.sep))
				for file in files:
					if os.path.join(src,file) not in ignore:
						print("Copying " + os.path.join(src,file) + "...")
						shutil.copy(os.path.join(src,file),os.path.join(dst,file))

if __name__ == "__main__":
	args = utils.args()
	copy(args['src'],args['dst'])
