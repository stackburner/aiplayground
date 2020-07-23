# -*- coding: utf-8 -*-
"""
# Name: plotter.py
# Description: This script plots graphs using matplotlib
# Owner: Lennart Berning
# Prerequisite: Matplotlib and Numpy
# Python Version: 3.7
"""

# Imports
import os
path = os.path.join(os.path.dirname(__file__), 'static/plots')
from sys import platform
if platform == 'linux' or platform == 'linux2':
    os.environ['MPLCONFIGDIR'] = path
import matplotlib.pyplot as plt
import numpy as np


def plot_sigmoid(prob=0.5, path=path):
    save_path = os.path.join(path, 'sigmoid.png')
    if os.path.exists(save_path):
        os.remove(save_path)

    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    def inv_sigmoid(x):
        return np.log(x/(1-x))

    z = np.arange(-7, 7, 0.1)
    phi_z = sigmoid(z)
    plt.title('Sigmoidal Logistic Function')
    plt.plot(z, phi_z)
    plt.plot(inv_sigmoid(prob), prob, 'r*')
    plt.axvline(0.0, color='k')
    plt.xlabel('z')
    plt.ylabel('$\phi (z)$')
    plt.yticks([0.0, 0.5, 1.0])
    ax = plt.gca()
    ax.yaxis.grid(True)
    plt.savefig(save_path)
    plt.clf()
    return save_path[save_path.find('/static'):]
