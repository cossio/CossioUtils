"""
Input/output with the CHO_K1 model files.
"""

import os
import subprocess


def gunzip(path):
    """
    Check if file is gzipped, in which case extract it. 
    Returns original path.
    """
    if os.path.exists(path + '.gz'):
        subprocess.call(['gunzip', '--keep', path + '.gz'])
    elif not os.path.exists(path):
        raise FileNotFoundError        
    return path


def gzip(path):
    """
    Compress file. Keeps original.
    """
    if os.path.exists(path):
        subprocess.call(['gzip', '--keep', '--force', path])
    else:
        raise FileNotFoundError
    return path
