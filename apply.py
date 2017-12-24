# TODO support for blacklist
# TODO 


import os
from subprocess import Popen
import sys

cwd = os.getcwd()
folders =  [folder for folder in os.listdir(cwd) if os.path.isdir(folder)]

argIndex = 1

shell = "c:\\Windows\\System32\\cmd.exe"
shellargs = ["/C"]

executable = sys.argv[argIndex]
argIndex += 1
if os.path.isfile(cwd + "\\" + executable):
  executable = cwd + "\\" + executable

arguments = sys.argv[argIndex:] if argIndex < len(sys.argv) else []

cmd = [shell] + shellargs + [executable] + arguments 

print("Arguments: " + ", ".join(sys.argv))
print("Current working directory: " + cwd)
print("Command to be executed: " + " ".join(cmd))

for folder in folders:
    print("\n------------------------- Working on folder " + folder + " -------------------------")
    p = Popen(cmd, cwd=folder)
    stdout, stderr = p.communicate()
print("Worked on " + ", ".join(folders))