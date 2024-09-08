# aggregate_data.py
import sys
import pandas as pd
import matplotlib.pyplot as plt
import logging, traceback

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error(''.join(["Uncaught exception: ",
                         *traceback.format_exception(exc_type, exc_value, exc_traceback)
                         ])
                 )
# Install exception handler
sys.excepthook = handle_exception


def main(input_files,output_csv, output_png):
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
    #1/0

if __name__ == '__main__':
    if 'snakemake' in globals():
        logging.basicConfig(filename=snakemake.log[0],
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
        # Accessing Snakemake variables
        input_files = list(snakemake.input)
        output_csv = str(snakemake.output[0])
        output_png = str(snakemake.output[1])
        logging.info(f'aggregate data: {input_files=}')
    else:
        # do classical optparsing
        pass # not implemented
    
    main(input_files, output_csv, output_png)
