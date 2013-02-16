#! /usr/bin/env python2
import os
import sys
import md5
def indexfile(dbfile, infile):
  filehash = md5.md5(infile).hexdigest()
  print(filehash)
  hashes = dbfile.read().split("\n")
  if filehash in hashes:
    print("File already indexed")
  else:
    dbfile.write(filehash + "\n")
if len(sys.argv) > 1:
  if os.path.isfile(sys.argv[1]):
    indexfile(open('database', 'r+a'), open(sys.argv[1]).read())
  elif sys.argv[1] == "--clear" or sys.argv[1] == "-c":
    open('database', 'w').write("")
  else:
    print("File not found: " + sys.argv[1])
