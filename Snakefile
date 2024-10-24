# Snakefile

# Configurations
report: 
    "report/workflow.rst", 

# Load configuration
configfile: "config/config.yaml"
# Access configuration parameters
SAMPLES = config["samples"]

wildcard_constraints:
    sample="[^/]+",


rule all:
    input:
        expand("results/plots/{sample}.png", sample=SAMPLES),
        "results/summary.csv",
        "results/summary.png"

rule generate_data:
    output:
        report("results/data/{sample}.csv", caption="report/tables.rst", category="Data Generation")
    params:
        n = config['generate_data']['n']
    benchmark:
        "logs/benchmark/create_{sample}.txt"
    script:
        "scripts/generate_data.py"

rule plot_data:
    input:
        "results/data/{sample}.csv"
    output:
        report("results/plots/{sample}.png", 
               caption="report/images.rst", 
               category="Data Visualization")
    benchmark:
        "logs/benchmark/plot_{sample}.txt"
    script:
        "scripts/plot_data.py"

rule aggregate_data:
    input:
        expand("results/data/{sample}.csv", sample=SAMPLES)
    output:
        report("results/summary.csv", category="Aggregation", caption="report/tables.rst"),
        report("results/summary.png", category="Aggregation", caption="report/images.rst")
    benchmark:
        "logs/benchmark/aggregate.txt"
    log:
        "logs/aggregate.txt"
    script:
        "scripts/aggregate_data.py"