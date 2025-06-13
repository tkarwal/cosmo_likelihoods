# SPT Muse 3G 
### Likelihood for MontePython 

MontePython wrapper for SPT lensing and EE likelihood by Tanvi Karwal with input from Fei Ge 

## Instructions 

1) Wherever you keep your likelihoods that are accessible by both MontePython and Cobaya, do 
```
wget https://pole.uchicago.edu/public/data/ge25/muse_3g_like_march_2025.zip
```
(skip this step if you already have SPT muse 3G pip installed previously)

2) Untar 

3) Go into the folder and `pip install`

4) Copy the `SPT_muse_3g_like_march_2025` folder into `/montepython_public/montepython/likelihoods`  such that you now have a folder `/montepython_public/montepython/likelihoods/SPT_muse_3g_like_march_2025` with files including `__init__.py`

5) Include the SPT muse 3G likelihood in your likelihoods block of the param file as 

```
data.experiments=['SPT_muse_3g_like_march_2025']
```

6) Choose whether you want just the lensing or just the polarisation part of the likelihood by accordingly setting the following variable in your `log.param` file 
```
SPT_muse_3g_like_march_2025.components = ['ϕϕ', 'EE']
```
