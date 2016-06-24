# -*- coding: utf-8 -*-

#Dieses Programm löst das SIR-Modell - hoffentlich bald.
#von Jana Lutz und Aaltje Mazur

from numpy import array, exp, zeros
from scipy.linalg import solve
from scipy.optimize import fsolve
from matplotlib import use
use('TkAgg')
from matplotlib.pyplot import (axis,
            close,
            legend,
            plot,
            rcParams,
            show,
            title,
            xlabel,
            ylabel,
            yscale,
            xscale)
from pylab import savefig

