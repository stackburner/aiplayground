# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import aiplayground.main
import os
import sys
from sys import platform
import logging
log = os.path.join(sys.path[0], 'aiplayground.log')
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=log,
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
if platform != 'linux' and platform != 'linux2':
    app.run()