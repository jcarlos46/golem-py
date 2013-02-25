import os.path

def remote_exists(sftp, path):
    """os.path.exists for paramiko's SCP object
    """
    try:
        sftp.stat(path)
    except IOError, e:
        if e[0] == 2:
            return False
        raise
    else:
        return True

def exists(path, sftp=None):
    if sftp:
        return remote_exists(sftp, path)
    else:
        return os.path.exists(path)