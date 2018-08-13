from __future__ import division
import numpy as np
import scipy

eps = 1e-8

def normalise_map(m):
	return (m - np.mean(m)) * 1. / np.std(m)