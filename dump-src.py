# dump-src.py
# author: Christophe VG

# small wrapper around the foo-lang parser to parse and dump the parse source

import sys

from foo_lang import api

if len(sys.argv) < 2:
  print "ERROR: please provide a foo-lang source file"
  sys.exit(2)

input = open(sys.argv[1]).read()
model = api.load(input)
print model
