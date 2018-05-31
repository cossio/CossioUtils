"""
Input/output with the CHO_K1 model files.
"""

import os
import subprocess


def gunzip(path, keep=True):
    """
    Check if file is gzipped, in which case extract it (replacing output). 
    Returns original path.
    """
    if os.path.exists(path + '.gz'):
        if keep:
            subprocess.call(['gunzip', '--force', '--keep', path + '.gz'])
        else:
            subprocess.call(['gunzip', '--force', path + '.gz'])
    elif not os.path.exists(path):
        raise FileNotFoundError        
    return path


def gzip(path, keep=True):
    "Compress file (replacing output)."
    if os.path.exists(path):
        if keep:
            subprocess.call(['gzip', '--force', '--keep', path])
        else:
            subprocess.call(['gzip', '--force', path])
    else:
        raise FileNotFoundError
    return path
