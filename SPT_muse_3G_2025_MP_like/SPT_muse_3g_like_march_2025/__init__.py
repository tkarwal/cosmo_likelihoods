'''
Written by Tanvi Karwal with input from Fei Ge 
'''

import muse3glike 
import montepython.io_mp as io_mp
from montepython.likelihood_class import Likelihood
import numpy as np

class SPT_muse_3g_like_march_2025(
    Likelihood,
    muse3glike.spt3g_2yr_delensed_ee_optimal_pp_muse
    ):

    # initialization routine

    def __init__(self, path, data, command_line):

        Likelihood.__init__(self, path, data, command_line)

        if not "ϕϕ" in self.components:
            self.requested_cls = ["pCl"]
        elif not "EE" in self.components:
            self.requested_cls = ["lCl"]
        else: 
            self.requested_cls = ["pCl", "lCl"]

        self.need_cosmo_arguments(data, {"output": ",".join(self.requested_cls), 'l_max_scalars':self.lmax})

    def initialize(self):
        muse3glike.spt3g_2yr_delensed_ee_optimal_pp_muse.__init__(self, filename=None, components=self.components)

    # compute likelihood
    def logp(self, cosmo, **kwargs):
        ℓ_slice = slice(self.BPWF["ℓ"][0], self.BPWF["ℓ"][-1] + 1)
        ee_array = np.asarray( self.get_unlensed_cl(cosmo, self.lmax)["ee"][ℓ_slice] )
        pp_array = np.asarray( self.get_cl(cosmo, self.lmax)["pp"][ℓ_slice] )
        return self.loglike({
            "EE": ee_array if "EE" in self.components else None,
            "ϕϕ": pp_array if "ϕϕ" in self.components else None
        })

    def loglkl(self, cosmo, data):

        self.initialize()

        return self.logp(cosmo=cosmo)
