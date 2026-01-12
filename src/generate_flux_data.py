import numpy as np
import pandas as pd

np.random.seed(42)

# position in from cm 
x = np.linspace(0,100,100)

# Neutron flux model 
phi_0 = 1e13    # n/cm^2/s 
L = 30          # diffusion length (cm)
noise = np.random.normal(0,1e11,size=len(x))

flux = phi_0*np.exp(-x/L)+noise 

# create dataframe
df = pd.DataFrame({
    "position_cm": x,
    "neutron_flux": flux
})

# save to csv
df.to_csv("data/neutron_flux.csv", index = False)
print("Data saved to data/neutron_flux.csv")
