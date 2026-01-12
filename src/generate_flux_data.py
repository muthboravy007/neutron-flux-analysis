import numpy as np
import pandas as pd

np.random.seed(42)

# position in from cm 
x = np.linspace(0,100,100)

# Neutron flux model 
phi_0 = 1e13  # Initial neutron flux in n/cm²/s
L1 = 20  # Region 1 diffusion length in cm
L2 = 50  # Region 2 diffusion length in cm

noise1 = np.random.normal(0,1e11, size=len(x))
noise2 = np.random.normal(0,1e11, size=len(x)) 

flux_region1 = phi_0 * np.exp(-x/L1) + noise1 
flux_region2 = phi_0 * np.exp(-x/L2) + noise2

df = pd.DataFrame({
    "position_cm": x,
    "neutron_flux_region1": flux_region1,
    "neutron_flux_region2": flux_region2
})

df.to_csv("data/neutron_flux_data.csv", index=False)
print("Data saved to data/neutron_flux_data.csv")


