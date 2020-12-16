import subprocess

def install_requirements_RL():
    process = subprocess.run(['sh install_requirements_RL.sh'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True,                         
                         shell=True)
    return process.stdout
