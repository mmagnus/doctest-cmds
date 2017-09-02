#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from __future__ import print_function
import argparse
import subprocess

def run_cmd(cmd):
    o = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = o.stdout.read().strip().decode()
    err = o.stderr.read().strip().decode()
    return out, err


def is_ok(fn):
    no_test = True
    for l in open(fn):
        if '   $ ' in l: # intended lines with $
            out, err = run_cmd(l.strip().replace('$', ''))
            no_test = False
            if err:
                print(out)
                print(err)
                return False
    if no_test:
        return False  # broken
    return True

if __name__ == '__main__':
    fn = "rna_filter.py"
    doctest_cmds(fn)
