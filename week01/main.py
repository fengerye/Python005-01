#import say_hello
import time
#import datetime
import logging
import os
#import re
#import pathlib

def say():
	logging.info('I say :"good good study, day day up!"')
	print("I will use python")

today = time.strftime('%Y-%m-%d',time.localtime())
path = "/var/log/python-" + today +"/"
#print(path)
try:
	os.chdir(path)
except:
	os.mkdir(path)
	os.chdir(path)
logging.basicConfig(filename="say.log",level=logging.INFO,datefmt="%Y-%m-%d %H:%M:%S",format="%(asctime)s %(name)-8s %(levelname)-8s[line: %(lineno)d] %(message)s")

say()

logging.warning("over")

