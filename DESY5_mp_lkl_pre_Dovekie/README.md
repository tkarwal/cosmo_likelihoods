# DES Y5 Supernovae
### Likelihood for MontePython 

Tanvi Karwal hacking together a version of the DES Y5 Supernova likelihood with input from Dillon Brout

Using the Pan+ likleihood as a base and simply modifying the data and covmat files to point instead to DES Y5

## Instructions 

1) Copy the DESY5 data to the `montepython_public/data/` folder in MP. 
   So you should now have a folder `montepython_public/data/DESY5_SNe` with files including `DESY5_SNe.dataset`
2) Copy the likelihood folder to `/montepython_public/montepython/likelihoods`  such that you now have a folder `/montepython_public/montepython/likelihoods/DESY5_SNe` with files including `__init__.py`
3) Include the DES Y5 likelihood in your likelihoods block of the param file as 

```
data.experiments=['DESY5_SNe']
```

4) Just as for the former Pantheon data, the only nuisance parameter is "M" the SN1a intrinsic magnitude. Don't forget to include it in a run:
```
data.parameters['M'] = [-19.2, -30, -10, 0.05, 1, 'nuisance']
```
