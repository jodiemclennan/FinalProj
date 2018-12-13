#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:13:26 2018

@author: rachelbarron
"""
import numpy as np
from scipy.integrate import quad




buNum = 6 # number of bunches @Fermilab tevatron number of bunches in 1 dir
bunLen = .06 # m (can range from a few to 50 cm)
sigX = .1 # cm gaussian rms radii wrt x: for now assume all radii to be equal
sigY = .01 # cm gaussian rms radii wrt y


lght = 2.99e8 # m/s

#ken = .5*m*omega**2
enPart = 2/6.242e9

bendRad = ''
#potEn = 88e3*enPart**4/(lght**2*bendRad)
enLoss = (88/lght**2)
freq = 10**6 # sec^-1 rev freq
iBun = 10**-3 # mA/bunch at 2GeV

massPart = 9.11e-31
gammaPart = enPart/massPart # we think gamma = c^2 = E/mass_e-

radPart = 2.82e-15 # m radius of particles (electron and positron)
 
betaX = np.linspace(.1,1,100) # amplitude functions at interaction point

crossA = 4*np.pi*sigX*sigY
# Think that these vals are wrong... check interp of nums
nElMax = gammaPart*2*np.pi*sigX*(sigX + sigY) * .06/(radPart*betaX)
nPosMax = gammaPart*2*np.pi*sigX*(sigX + sigY) * .06/(radPart*betaX)

eChar = 1.6027e-19 # Coulombs
k = 1/(4*np.pi*eChar**2)

lum = nElMax*nPosMax*buNum*freq/(4*np.pi*sigX*sigY)
evRat = lum*crossA # event rate N

iDens = nPosMax*freq*buNum
