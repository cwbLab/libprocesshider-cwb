#!/usr/bin/python
import sys
import time

number =  sys.argv[1]

for i in range( 1 , int(  number )  ):
  time.sleep(2)
  print(i)
