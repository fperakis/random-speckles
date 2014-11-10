'''
A simple program for simulating a speckle pattern form a distribution of random phasors. 
See book: "Speckle phenomena in optics: Theory and applications", J.W.Goodman, 2007
Adapted from Appendix G
'''

import numpy as np
import time
from matplotlib import pyplot as plt

#parameters
asicshape = [100,100]#[185,194]
specklesize = 5
ld = 21 # maximum distance (pixels)

#definitions 
nasic = asicshape[0]*asicshape[1]
photons = np.zeros(asicshape)

#definitions speckles
randphasors = np.zeros([asicshape[0],asicshape[1]],dtype = complex)
nphasorsx = np.round(asicshape[0]/specklesize).astype(int)
nphasorsy = np.round(asicshape[1]/specklesize).astype(int)

#random phasors
for i in range(nphasorsx):
    for j in range(nphasorsy):
        randphase = np.random.random_sample()*2.j*np.pi
        randphasors[i,j] = np.exp(randphase)

#speckles
specklefield = np.fft.fft2(randphasors)
speckleint = np.absolute(specklefield)*np.absolute(specklefield)
speckleint/=np.sum(speckleint)
photons = speckleint

#plot 
plt.close('all')
plt.figure(1)
plt.imshow(speckleint,interpolation='none',cmap ='hot')
plt.show()   