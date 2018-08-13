
from __future__ import division
import numpy as np
import scipy
from utils import *


def KLdiv(salmap, fixmap):
	if salienceMap != fixationMap.shape:
		salmap = scipy.misc.imresize(salmap, fixationMap.shape)

	#normalise into distribution
	salmap = salmap / np.sum(salmap)
	fixmap = fixmap / np.sum(fixmap)

	#compute KL divergence
	return np.sum(fixmap * np.log2(eps + salmap / eps+fixmap))
