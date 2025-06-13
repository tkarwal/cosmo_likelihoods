import os
import numpy as np
from montepython.likelihood_class import Likelihood
import montepython.io_mp as io_mp
import warnings

class bao_DESI_DR2(Likelihood):

    # initialization routine
    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)

        self.data_file = os.path.join(self.data_directory, self.bao_data)
        self.cov_file = os.path.join(self.data_directory, self.cov)

        self.z         = np.loadtxt(self.data_file, usecols=(0))
        self.bao_value = np.loadtxt(self.data_file, usecols=(1))
        self.bao_type  = np.loadtxt(self.data_file, usecols=(2,), dtype=str)

        self.cov       = np.loadtxt(self.cov_file)
        self.inv_cov   = np.linalg.inv(self.cov)

    # compute likelihood
    def loglkl(self, cosmo, data):
        chi2 = 0.
        
        self.theory_arr = np.zeros(self.bao_type.shape)

        for i in range(len(self.bao_type)):
            if 'DV' in self.bao_type[i]:
                DA = cosmo.angular_distance(self.z[i])
                DR = self.z[i] / cosmo.Hubble(self.z[i])
                rs = cosmo.rs_drag()
                DV = pow(DA * DA * (1 + self.z[i]) * (1 + self.z[i]) * DR, 1. / 3.)
                DV /= rs
                self.theory_arr[i] = DV
                # print(DV)
            elif 'DM' in self.bao_type[i]:
                DM = (1+self.z[i]) * cosmo.angular_distance(self.z[i]) /  cosmo.rs_drag()
                self.theory_arr[i] = DM
                # print(DM)
            elif 'DH' in self.bao_type[i]:
                DH = 1. / cosmo.Hubble(self.z[i]) /  cosmo.rs_drag()
                self.theory_arr[i] = DH
                # print(DH)

        self.Delta_vec = self.bao_value-self.theory_arr

        chi2 += np.dot(np.dot(self.Delta_vec,self.inv_cov),self.Delta_vec)
        lkl = - 0.5 * chi2

        return lkl