# flex-ddg-automation

This tool is built based on [flex_ddG_tutorial](https://github.com/Kortemme-Lab/flex_ddG_tutorial)

## Folder structure

- `ddG-backrub.xml` `ddG-no_backrub_control.xml` `ddG.db3` `split_protocol` are configuration files that define rosseta ddg behaviour, such as score function, etc. 

- `run_example_2_saturation.py` is the template python file based on [flex_ddG_tutorial example 2](https://github.com/Kortemme-Lab/flex_ddG_tutorial/blob/master/run_example_2_saturation.py), including some code templates, such as mutation `residue`, output path, `nstruct`, etc... which could be reused by multiple setups

- `analysis.py` is the template python file based on [flex_ddG_tutorial analyze_flex_ddG](https://github.com/Kortemme-Lab/flex_ddG_tutorial/blob/master/analyze_flex_ddG.py)

- `setup-ddg.py` `ddg-analysis.py` are scripts that help set up and analysis flex-ddg in bulk with a list of mutation

- `run-mut.sh` is the shell file that is used by [RCCS super computer system](https://ccportal.ims.ac.jp/en/QuickStart#buildrun_command) to run flex-ddg program

- `job-submit.py` is used to submit execution job (`run-mut.sh`) to super computer in bulk

## Usage

### setup all source code and inputs
```bash
# Syntax: python3 setup-ddg.py /PATH/TO/PDB RESIDUE_LIST /PATH/TO/OUTPUT

# example

[@rosetta-automation/flex-ddg-automation]$ python3 setup-ddg.py ~/dimer.pdb 303,304,305,333,369,373,377,426,427,469 C ~/MET-NK1-ddG

```

### submit all execution jobs
```bash
# Example
[@rosetta-automation/flex-ddg-automation]$ python3 job-submit.py ~/MET-NK1-ddG
```

### analyze result
```
# Example
[@rosetta-automation/flex-ddg-automation]$ python3 ddg-analysis.py ~/MET-NK1-ddG
```