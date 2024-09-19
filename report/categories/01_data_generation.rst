Data Generation
===============
The first step of this workflow is the creation of random data. 
For each sample, {{snakemake.config["data_generation"]["n"]}} 
data points are drawn from a standard normal distribution and saved as .csv file. 