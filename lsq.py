
from __future__ import division
import numpy as np
import scipy
from utils import *

def least_squares(salmap, fixmap):
	if salmap.shape != fixmap.shape:
		salmap = scipy.misc.imresize(salmap, fixmap)

	salmap = normalise_map(salmap)
	fixmap = normalise_map(fixmap)

	return np.sum(np.square(salmap - fixmap))
