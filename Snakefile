# Snakefile

# Configurations
report: "report/workflow.rst"
# Load configuration
configfile: "config/config.yaml"
# Access configuration parameters
SAMPLES = config["samples"]

rule all:
    input:
        expand("results/plots/{sample}.png", sample=SAMPLES),
        "results/summary.csv",
        "results/summary.png"

rule generate_data:
    output:
        report("results/data/{sample}.csv", category="Data Generation")
    params:
        n = config['generate_data']['n']
    script:
        "scripts/generate_data.py"

rule plot_data:
    input:
        "results/data/{sample}.csv"
    output:
        report("results/plots/{sample}.png", caption="report/caption.rst", category="Data Visualization")
    script:
        "scripts/plot_data.py"

rule aggregate_data:
    input:
        expand("results/data/{sample}.csv", sample=SAMPLES)
    output:
        report("results/summary.csv", category="Aggregation"),
        report("results/summary.png", category="Aggregation")
    script:
        "scripts/aggregate_data.py"