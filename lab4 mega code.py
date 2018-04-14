import cmath as math
from numpy import sqrt, pi, exp, linspace, loadtxt
import numpy as np
from lmfit import Model
import matplotlib.pyplot as plt
from scipy import special, integrate

five = np.loadtxt("C:\\Users\\윤예지\\Downloads\\lab4.txt")
eightpointfive = np.loadtxt("C:\\Users\\윤예지\\Downloads\\eightpointfive.txt")

class lab4:

    def __init__(self, name, x, y, amp, cen, wid, off):
        self.name = name
        self.x = x[:]
        self.y = y[:]
        self.amp = amp
        self.cen = cen
        self.wid = wid
        self.off = off


    def data(self):

        plt.scatter(self.x, self.y, label = "Data")
        plt.xlabel("Angular Separation")
        plt.ylabel("Coincidence Counts in 10 seconds")
        plt.title("Correlation Function for Annihilation of Na22")
        plt.legend()

    def fit(self):
        def gaussian(x, amp, cen, wid, off):
            """gaussian function, guess x, amp, cen, wid"""
            return (amp / (sqrt(2 * pi) * wid)) * exp((-(x - cen) ** 2) / (2 * wid ** 2)) + off

        gmodelfit = Model(gaussian).fit(self.y, x=self.x, amp=self.amp, cen=self.cen, wid=self.wid, off=self.off)
        plt.plot(self.x, gmodelfit.best_fit, label="gaussian fit", color="g", lw=1, ls='--')
        print(gmodelfit.fit_report())


aa = lab4("5 inches apart", five[:,0], five[:,1], 500, 180, 5, 5)
aa.data()
aa.fit()
bb = lab4("8.5 inches apart", eightpointfive[:,0], eightpointfive[:,1], 190, 180, 5, 5)
bb.data()
bb.fit()
plt.show()
