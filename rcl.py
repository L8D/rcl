#! /usr/bin/env python2
import sys
import md5
dbfile = open('database')
print(dbfile.read())
print(md5.md5(dbfile.read()).hexdigest())
filehash = md5.md5(open(sys.argv[1]).read()).hexdigest()
print(filehash)
