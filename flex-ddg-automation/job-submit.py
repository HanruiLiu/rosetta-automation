# python3 job-submit.py ~/MET-NK1-DDG

import sys
import os
import subprocess

destination_path = os.path.abspath(sys.argv[1])

all_jobs_list = os.listdir(destination_path)

for job_directory in all_jobs_list:
    # job_directory = 300, jsub -q PN /home/usr/cei/MET-NK1-DDG/300/run-mut.sh
    command = ['jsub', '-q', 'PN', os.path.join(destination_path, job_directory, 'run-mut.sh')]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
