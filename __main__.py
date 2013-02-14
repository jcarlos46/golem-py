#!/usr/bin/env python
from copy import copy
from zip import zip
from utils import args

if __name__ == "__main__":
	print("=golem at work=")
	args = args()
	zip(args['src'], args['dst'])
	copy(args['src'], args['dst'])
