#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/aiplayground/")
sys.path.insert(0,"/var/www/aiplayground/aiplayground/")
 
from aiplayground import aiplayground as application
application.secret_key = 'porsche'

