#! /usr/bin/env python2
import os, sys, hashlib


#            String name of database file
#             |   String name of input file
#             |    |
def indexfile(db, inp):

  # Open the files
  infile = open(inp).read()
  dbfile = open(db, 'r+a')

  # Create hash and hash table from database
  filehash = hashlib.sha512(infile).hexdigest()
  hashes = dbfile.read().split("\n")
  for x, i in enumerate(hashes):
    hashes[x] = i[0:128]

  # Check if hash is in table already
  if filehash in hashes:
    print("File already indexed")

  # Add hash and filesize to database
  else:
    dbfile.write(filehash + " Size: " + str(os.path.getsize(inp)) + "\n")
    print("Cached: " + filehash)


if len(sys.argv) > 1:

  # Check if the first arguement is a file
  if os.path.isfile(sys.argv[1]):
    indexfile('database', sys.argv[1])

    # Ask the user if they're sure they want to delete their file
    print("Are you sure? [Y/n]"),
    uc = raw_input()

    if uc in ['y', 'Y', 'yes' ]:
      os.remove(sys.argv[1])
      print('Deleted')

    else:
      print('Canceled')

  # Simple clear function to erase the database
  elif sys.argv[1] == "--clear" or sys.argv[1] == "-c":
    open('database', 'w').write("")

  # Function for simply hashing the file and not prompting for deletion
  elif sys.argv[1] == "--hash" or sys.argv[1] == "-h":
    indexfile('database', sys.argv[2])

  # Function for forcing the deletion with no prompt
  elif sys.argv[1] == "--force" or sys.argv[1] == "-f":
    indexfile('database', sys.argv[2])
    os.remove(sys.argv[2])
    print('Deleted')

  # Function to assign custom database; Switches indexfile arguements
  elif sys.argv[1] == "--database" or sys.argv[1] == "-d":
    indexfile(sys.argv[2], sys.argv[3])

  # If the first arguement doesn't match any options or isn't a file, print this
  else:
    print("File not found: " + sys.argv[1])

# If nothing is written, then just print usage
else:
  print("Usage: rcl [-cdh] <filename>")
