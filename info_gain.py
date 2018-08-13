
from __future__ import division
import numpy as np
import scipy


def info_gain(salienceMap, fixationMap, baselineMap):
	# finds the information gain of the saliency map over a baseline map
	if salienceMap.shape != fixationMap.shape:
		salienceMap = scipy.misc.imresize(salienceMap, fixationMap.shape)

	if baseline.shape != fixationMap.shape:
		baselineMap = scipy.misc.imresize(baselineMap, fixationMap.shape)

	# normalise arrays
	salienceMap = normalise_map(salienceMap)
	baselineMap = normalise_map(baselineMap)
	# vectorise the arrays!
	salienceMap = np.ndarray.flatten(salienceMap)
	baselineMap = np.ndarray.flatten(baselineMap)

	# normlise into probability distributions
	salienceMap = salienceMap * 1./np.sum(salienceMap)
	baselineMap = baselineMap * 1./np.sum(baselineMap)

	# this is wrong... nottotally sure where theactual fixation map comes in?
	# anyhow... it's all based on this paper: http://www.pnas.org/content/112/52/16054.abstract
	return np.mean(np.log2(eps + salienceMap) - np.log2(eps+baselineMap))
