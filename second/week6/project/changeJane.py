#!/usr/bin/env python3

import sys
import subprocess

def main(file):
    new = []
    old = []
    with open(file) as f:
        old = [line.strip() for line in f]
        new = [line.replace("jane", "jdoe") for line in old]
    return (old, new)


old, new = main(sys.argv[1])
print(old)
print(new)
for oldname, newname in zip(old, new):
    subprocess.run("mv {} {}".format(oldname, newname), shell=True)