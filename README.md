
# Basic Snakemake Workflow


This Snakemake workflow demonstrates a basic data analysis pipeline for generating random datasets, 
plotting individual samples, and aggregating the data to create a summary table and plot. 
The pipeline is designed to test Snakemake's reporting functionality and showcases the use of the `report()` 
directive to include results in a final HTML report. It is suited to test new features. 

## Workflow Steps

* **Data Generation:** For each of the samples, random data is generated using a normal distribution. 
* **Data Visualization**:  Each sample's data is visualized in a plot. 
* **Data Aggregation**: All generated data files are aggregated into a single summary file. 

## Configuration

The workflow can be configured in the `config.yaml` file. 
In particular a list of `samples` and the number of data points `n` per sample in the data generation step can be provided. 

## Results
The workflow generates:

* Plots of individual sample data.
* A summary table of aggregated data.
* A summary plot.

