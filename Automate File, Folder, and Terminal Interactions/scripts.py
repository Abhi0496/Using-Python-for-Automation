#it contains automated terminal logic
#subprocess is a library that allows our python script to interact with the command line interface
#check_call() runs a executable in terminal and waits untill the process has finished 

import subprocess

for i in range(5):
    subprocess.check_call(['python3','helloworld.py'])

    #its basically running the command- python3 helloworld.py 5 times
