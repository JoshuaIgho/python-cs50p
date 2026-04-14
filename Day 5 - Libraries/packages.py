#Third party libraries - pypi.org
#the lesson said use pip install cowsay but use python3 -m pip install cowsay


import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])