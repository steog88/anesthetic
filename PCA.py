%load_ext autoreload
%autoreload 2

from anesthetic.kde import load_nested_samples

# Load the samples
samples = load_nested_samples('/data/will/data/pablo/runs/chains/planck')

h = samples['H0']/100
samples['omegab'] = samples['omegabh2']/h**2
samples.tex['omegab'] = '\Omega_b'
samples['omegac'] = samples['omegach2']/h**2
samples.tex['omegac'] = '\Omega_c'

paramnames = ['omegam', 'sigma8']#, 'theta', 'tau', 'logA', 'ns']
fig, axes = samples.plot_2d(paramnames)

samples_2 = load_nested_samples('/data/will/data/pablo/runs/chains/DES')
samples_3 = load_nested_samples('/data/will/data/pablo/runs/chains/DES_planck')

samples_2.plot_2d(paramnames, axes=axes, color='r')
samples_3.plot_2d(paramnames, axes=axes, color='g')


fig, axes = samples.plot_2d(paramnames,['omegam', 'tau'])
