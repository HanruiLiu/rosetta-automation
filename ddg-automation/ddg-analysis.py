import sys
import os
import subprocess

folder_to_analysis = sys.argv[1]

mutation_to_analysis = os.listdir(folder_to_analysis)

for mutation_folder in mutation_to_analysis:
    output_folder = os.path.join(folder_to_analysis, mutation_folder, 'output_' + mutation_folder)
    command = ['python3', 'analysis.py', output_folder]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
