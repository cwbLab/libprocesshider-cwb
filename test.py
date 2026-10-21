#!/usr/bin/python
import sys
import time

number =  sys.argv[1]

for i in range( 1 , int( number )  ):
  print(i)
  time.sleep(5)
  
