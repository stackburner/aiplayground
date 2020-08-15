# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
import aiplayground.main
from sys import platform
if platform != 'linux' and platform != 'linux2':
    app.run()