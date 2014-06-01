
'''
    Calculate the md5 hash of a file
    Split file into blocks so the entire file doesn't have to be in memory
    Takes about 4.6 sec / GB and about 8kb of memory for any file size
    Make sure the file is open in rb mode
'''

import hashlib


def md5_file(fileobj):
    md5 = hashlib.md5()
    with fileobj as f:
        for chunk in iter(lambda: f.read(128 * md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

