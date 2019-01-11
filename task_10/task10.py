#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from shutil import copyfile

text = 'Some text that should be used right after runing program'


def write2begin(text, offset=34, step=2000, src='start.bmp', dest='result.bmp'):
    copyfile(src, dest)

    f = open(dest, 'r+b')

    f.seek(offset)
    for i in text:
        f.write(bytearray(i, 'UTF-8'))
        f.seek(step, 1)

    f.flush()
    f.close()


def read_from_begin(size, offset=34, step=2000, src='result.bmp'):
    f = open(src, 'r+b')

    f.seek(offset)
    result = b''
    for i in range(size):
        result = result + f.read(1)
        f.seek(step, 1)
    f.close()
    return result


write2begin(text)
print(read_from_begin(74))


