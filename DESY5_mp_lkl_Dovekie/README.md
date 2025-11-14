# DES Y5 Supernovae
### Likelihood for MontePython 

Tanvi Karwal hacking together a version of the DES Y5 Supernova likelihood by cannibalising the [likelihood](https://github.com/des-science/DES-SN5YR/blob/main/4_DISTANCES_COVMAT/DES-Dovekie-SN_Likelihood.py) that accompanied the release paper. 

## Instructions 

1) Copy the DESY5 data to the `montepython_public/data/` folder in MP. 
   So you should now have a folder `montepython_public/data/DESY5_SNe` with files including `DESY5_SNe.dataset`
2) Copy the likelihood folder to `/montepython_public/montepython/likelihoods`  such that you now have a folder `/montepython_public/montepython/likelihoods/DESY5_SNe` with files including `__init__.py`
3) Include the DES Y5 likelihood in your likelihoods block of the param file as 

```
data.experiments=['DESY5_SNe']
```

4) This is written to marginalise over the absolute magnitude M following the way it was done in the likelihood released with the paper. So no nuisance parameters. 
