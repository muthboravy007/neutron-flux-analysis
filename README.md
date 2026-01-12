# Neutron Flux Analysis

## MUTH Boravy

This project demonstrates a simple data science workflow applied to a nuclear engineering problem.

## Project Overview

Neutron flux distribution in a reactor core is analyzed using synthetic data generated from an exponential attenuation model. The project includes data generation, exploratory analysis, and parameter estimation using nonlinear regression.

## Repository Structure

- `data/` — synthetic neutron flux dataset  
- `src/` — data generation scripts  
- `notebooks/` — analysis and modeling notebook  

## Methods

- Synthetic data generation based on neutron diffusion theory
- Exploratory data analysis using pandas and matplotlib
- Exponential model fitting using nonlinear least squares

## Results

The neutron flux decreases exponentially with position. The fitted attenuation length is consistent with physical expectations for a simplified reactor model.

## Requirements

- Python 3.x
- numpy
- pandas
- matplotlib
- scipy

## How to Run

```bash
python src/generate_flux_data.py
