#!/usr/bin/env python

import sys
import os


# print(sys.argv)

file = sys.argv[1]

if os.path.exists(file):
    print("file already exist")
    sys.exit(20)
else:
    with open(file, "w") as f:
        f.write("file created\n")

# check exist status of last process echo $?