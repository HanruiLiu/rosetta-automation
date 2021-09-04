'''
python3 setup-ddg.py ~/dimer.pdb 100,101,102 C ~/destination
'''

import os
import sys
from shutil import copyfile

if __name__=="__main__":
    path_to_pdb = os.path.abspath(sys.argv[1])
    pdb_basename = os.path.basename(path_to_pdb)

    residue_list = sys.argv[2]
    residue_list = residue_list.split(',')

    chains_to_move = sys.argv[3]

    destination_path = os.path.abspath(sys.argv[4])

    os.mkdir(destination_path)

## destination_path: ~/NK1 ,  /home/usr/cei/NK1/100/run-mut.sh
    for residue in residue_list:
        residue_ddg_path = os.path.join(destination_path, residue)
        os.mkdir(residue_ddg_path)
        copyfile('./ddG-backrub.xml', os.path.join(residue_ddg_path, 'ddG-backrub.xml'))
        copyfile('./ddG-no_backrub_control.xml', os.path.join(residue_ddg_path, 'ddG-no_backrub_control.xml'))
        copyfile('./ddG.db3', os.path.join(residue_ddg_path, 'ddG.db3'))
        copyfile('./run_example_2_saturation.py', os.path.join(residue_ddg_path, 'run_example_2_saturation.py'))
        copyfile('./run-mut.sh', os.path.join(residue_ddg_path, 'run-mut.sh'))

        run_mut_script = ''
        with open('./run-mut.sh') as f:
            run_mut_script = f.read()
            run_mut_script = run_mut_script.replace('{{PATH_TO_RESIDUE_DDG}}', residue_ddg_path)
        with open(os.path.join(residue_ddg_path, 'run-mut.sh'), 'w') as fileTowrite:
            fileTowrite.write(run_mut_script)

        run_example_2_saturation_script = ''
        with open('./run_example_2_saturation.py') as f:
            run_example_2_saturation_script = f.read()
            run_example_2_saturation_script = run_example_2_saturation_script.replace('{{CHAIN_TO_MOVE}}', chains_to_move)
            run_example_2_saturation_script = run_example_2_saturation_script.replace('{{RESIDUE}}', residue)
            run_example_2_saturation_script = run_example_2_saturation_script.replace('{{PATH_TO_RESIDUE_DDG}}', residue_ddg_path)
        with open(os.path.join(residue_ddg_path, 'run_example_2_saturation.py'), 'w') as fileTowrite:
            fileTowrite.write(run_example_2_saturation_script)

        os.mkdir(os.path.join(residue_ddg_path, 'inputs'))

        inputs_path = os.path.join(residue_ddg_path, 'inputs', pdb_basename)
        os.mkdir(inputs_path)

        copyfile(path_to_pdb, os.path.join(inputs_path, pdb_basename))
        with open(os.path.join(inputs_path, 'chains_to_move.txt'), 'w') as fileTowrite:
             fileTowrite.write(chains_to_move)
