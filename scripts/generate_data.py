# generate_data.py
import numpy as np
import pandas as pd

# Accessing Snakemake variables
n = snakemake.params.n
output_file = str(snakemake.output[0])

# Generate random data
np.random.seed(42)
data = pd.DataFrame({'x': range(1, n + 1), 'y': np.random.normal(loc=0, scale=1, size=n)})

# Save to CSV
data.to_csv(output_file, index=False)
