#! /usr/bin/python

import os
import time
print "hola mundo"
print "soy el proceso: ",os.getpid()
leido = os.read(0,1000)
#os.waitpid(pid,0)
print "chau, mi hijo termino"
