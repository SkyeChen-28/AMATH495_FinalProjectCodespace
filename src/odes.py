import numpy as np
from numpy.typing import NDArray
                  
class ClimateODEs:
    
    def __init__(self, G_r, G_p, K_r, K_p, gamma, alpha, beta, D, f) -> None:
        self.G_r = G_r
        self.G_p = G_p
        self.K_r = K_r
        self.K_p = K_p
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.D = D
        self.f = f
        self.innovation_const = 2e-1
    
    def dr_dt(self, t: float, y: NDArray) -> float:
        r = y[0]
        p = y[1]
        I_r = y[2]
        I_p = y[3]
        c = y[4]
        K_r = self.K_r
        G_r = self.G_r
        A = K_r * I_r
        return G_r * (1 - r/A) * r
    
    def dp_dt(self, t: float, y: NDArray) -> float:
        r = y[0]
        p = y[1]
        I_r = y[2]
        I_p = y[3]
        c = y[4]
        K_p = self.K_p
        G_p = self.G_p
        A = K_p * I_p
        return G_p * (1 - p/A) * p
    
    def dIr_dt(self, t: float, y: NDArray) -> float:
        # r = y[0]
        # p = y[1]
        # I_r = y[2]
        # I_p = y[3]
        # c = y[4]
        return self.innovation_const * self.dr_dt(t, y)
        # return self.innovation_const * r
    
    def dIp_dt(self, t: float, y: NDArray) -> float:
        # r = y[0]
        # p = y[1]
        # I_r = y[2]
        # I_p = y[3]
        # c = y[4]
        return self.innovation_const * self.dp_dt(t, y)
        # return self.innovation_const * p
    
    def dc_dt(self, t: float, y: NDArray) -> float:
        r = y[0]
        p = y[1]
        I_r = y[2]
        I_p = y[3]
        c = y[4]
        gamma = self.gamma
        alpha = self.alpha
        beta = self.beta
        A = alpha * I_r
        B = beta * I_p
        return gamma * (r/A + p/B)
        
    def vec_de(self, t: float, y: NDArray) -> NDArray:
        r = self.dr_dt(t, y)
        p = self.dp_dt(t, y)
        I_r = self.dIr_dt(t, y)
        I_p = self.dIp_dt(t, y)
        c = self.dc_dt(t, y)
        return np.array([r, p, I_r, I_p, c])
    
    def natural_disaster(self, year, f, GDP, c):
        '''
            Returns how much to reduce GDP by after the disaster
        '''
        D = self.D
        if ((year != 0) and (year % f == 0)):
            return 0.9 * GDP * (1 - np.exp(- D*c / GDP**2)) # Reduces r
        else:
            return 0
        