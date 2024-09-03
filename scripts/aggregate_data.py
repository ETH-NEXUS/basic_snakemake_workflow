# aggregate_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Accessing Snakemake variables
input_files = list(snakemake.input)
output_csv = str(snakemake.output[0])
output_png = str(snakemake.output[1])

# Aggregate data
dfs = [pd.read_csv(f) for f in input_files]
summary = pd.concat(dfs).groupby('x').mean().reset_index()

# Save summary table
summary.to_csv(output_csv, index=False)

# Plot summary
plt.figure()
plt.plot(summary['x'], summary['y'], label='Mean of samples')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Summary Plot')
plt.savefig(output_png)
plt.close()
