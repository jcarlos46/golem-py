import os, json, sys

def config(src):
	cfg = os.path.join(src,"config.json")
	f = open(cfg)
	j = json.load(f)
	j['self'] = cfg
	f.close()
	return j

def ignore(suffix,src): #monting list of ignored files
	c = config(src)
	ignore = [c['self']]
	for i in c['Ignore']:
		ignore.append(os.path.join(suffix,i))
	return ignore

def args():
	src = sys.argv[1]
	cfg = os.path.join(src,"config.json")
	if os.path.exists(cfg):
		c = config(src)
		if 'Destination' in c.keys():
			dst = c['Destination']
		else:
			dst = sys.argv[2]
	else:
		dst = sys.argv[2]
	return {'src':src,'dst':dst}
