import numpy as np
import matplotlib.pyplot as plt

input_dir = '/home/bruno/Desktop/'

#Load data from files
data = np.loadtxt( input_dir + 'mass_funtion.dat' )
halo_mass_warren = data[:,0]
mass_func_warren = data[:,1]
halo_mass_512 = data[:,2]
mass_func_512 = data[:,3]
halo_mass_1024 = data[:,4]
mass_func_1024 = data[:,5]


fig = plt.figure(0)
fig.clf()
ax = fig.add_subplot(111)
ax.plot(halo_mass_512, mass_func_512)
ax.plot(halo_mass_1024, mass_func_1024)
ax.plot(halo_mass_warren, mass_func_warren )
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'Mass $[{\rm M_{\odot}}h^{-1}]$', fontsize=15 )
ax.set_ylabel(r'n(>M)$[h^3{\rm Mpc^{-3}}]$', fontsize=15 )
plt.savefig( input_dir + 'mass_function.png', bbox_inches='tight', )
