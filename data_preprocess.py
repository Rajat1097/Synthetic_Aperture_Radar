import os
import subprocess

# Define the path to the SNAP executable
snap_bin_dir = 'C:/Program Files/snap/bin'

# Define the path to the saved preprocessing graph
graph_path = 'E:/EOGM/Dissertation/Practice_data/data_download/Graph.xml'

# Define the input directory containing the SAR data files
input_dir = 'E:/EOGM/Dissertation/Practice_data/data/data_download/'

# Define the output directory to store the preprocessed data
output_dir = 'E:/EOGM/Dissertation/Practice_data/data/data_preprocess/'

# List all SAR data files in the input directory
sar_files = [file for file in os.listdir(input_dir) if file.endswith('.zip')]

# Loop over each SAR data file
for sar_file in sar_files:
    # Construct the input and output file paths
    input_file = os.path.join(input_dir, sar_file)
    output_file = os.path.join(output_dir, os.path.splitext(sar_file)[
                               0] + '_preprocessed.dim')

    # Execute the preprocessing workflow using SNAP command-line tool
    command = f'"{snap_bin_dir}/gpt" "{graph_path}" -Pinput="{input_file}" -Poutput="{output_file}"'
    subprocess.call(command, shell=True)
