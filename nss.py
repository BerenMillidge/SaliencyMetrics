from __future__ import division
import numpy as np
import scipy
from utils import *

def NSS(salmap, fixmap):
	if salmap.shape != fixmap.shape:
		salmap = scipy.misc.imresize(salmap, fixmap)

	salmap = normalise_map(salmap)
	# fixmap should be binary
	# do it as a loop!
	# not sure if should be mean of whole thing... or only the mean values?
	# probably the latter, so I'll implement it myself
	h,w = salmap.shape
	total = 0
	N = 0
	for i in xrange(h):
		for j in xrange(w):
			if fixmap[i][j] != 0:
				total += salmap[i][j]
				N +=1

	return total/N
