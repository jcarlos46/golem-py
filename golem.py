import re
import argparse
import remote
import os
import utils
from hashlib import md5
from copy import copy
from paste import paste
from paths import paths
from zip import zip
from ignore import ignore
from exists import exists

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--backup')
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

regex = '.*@.*:\d+\/.*'
origin_src = 'remote' if re.match(regex, args.source) else 'local'
origin_dst = 'remote' if re.match(regex, args.destination) else 'local'

if __name__ == '__main__':
    print 'golem at work'
    sftp_src = remote.sftpclient(args.source) if origin_src == 'remote' else None
    sftp_dst = remote.sftpclient(args.destination) if origin_dst == 'remote' else None

    root_src = remote.info(args.source).root if origin_src == 'remote' else os.path.abspath(args.source)
    root_dst = remote.info(args.destination).root if origin_dst == 'remote' else os.path.abspath(args.destination)

    ignore = ignore(root_src + os.sep + 'config.json', sftp_src)

    if args.backup:
        print 'backuping folder ' + root_dst
        zip(root_dst, paths(root_dst, ignore, sftp_dst), args.backup, sftp_dst)

    for file_src in paths(root_src, ignore, sftp_src):
        file_dst = file_src.replace(root_src, root_dst)
        if utils.isdir(file_src, sftp_src):
            print 'creating folder ' + file_dst
            utils.mkdir(file_dst, sftp_dst)
        else:
            data_src = copy(file_src, sftp_src)
            if exists(file_dst):
                data_dst = copy(file_dst, sftp_dst)
                md5_data_src = md5(data_src).digest()
                md5_data_dst = md5(data_dst).digest()
                if md5_data_src == md5_data_dst:
                    print 'unchanged ' + file_dst
                else:
                    print 'modificing ' + file_dst
                    paste(file_dst, data_src, sftp_dst)
            else:
                print 'creating ' + file_dst
                paste(file_dst, data_src, sftp_dst)
    print 'golem finish'