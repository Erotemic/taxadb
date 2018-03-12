#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import sys
import logging


def md5_check(file, block_size=256*128):
    """Check the md5 of large files

    Args:
        file (:obj:`str`): input file
        block_size (:obj:`int`): block_size for the file chunks.
            Default = 256*128
    """
    logger = logging.getLogger(__name__)

    logger.info('Checking md5 of %s' % file)
    md5 = open(file + '.md5').readline().split()[0]
    file_md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            file_md5.update(chunk)
    assert(file_md5.hexdigest() == md5)
    logger.info('Checking md5 of %s: OK' % file)


def fatal(msg):
    """Prints a FATAL message and exit with status code 1

    Args:
        msg (:obj:`str`): Error message to print

    Raises:
        SystemExit

    """
    print("[FATAL] %s" % str(msg), file=sys.stderr)
    sys.exit(1)
