#!/usr/bin/env python
import os


print('Home: ' + os.getenv("home", ""))
print('Path: ' + os.getenv("path", ""))
print('Fruit: ' + os.getenv("fruit", ""))
