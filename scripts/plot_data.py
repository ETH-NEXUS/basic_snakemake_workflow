# plot_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Accessing Snakemake variables
input_file = str(snakemake.input[0])
output_file = str(snakemake.output[0])
sample = str(snakemake.wildcards.sample)

# Read data
data = pd.read_csv(input_file)

# Plot data
plt.figure()
plt.plot(data['x'], data['y'], label=sample)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Data Plot for {sample}')
plt.savefig(output_file)
plt.close()
