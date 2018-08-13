from __future__ import division
import numpy as np
import scipy
from utils import *

def correlation_coefficient(salmap, fixmap):
	#assert same shape , else resize
	if salmap.shape != fixmap.shape:
		salmap = scipy.misc.imresize(salmap, fixmap.shape)

	salmap = normalise_map(salmap)
	fixmap = normalise_map(fixmap)
	return scipy.stats.pearsonr(salmap, fixmap)