import os
import sys

if (len(sys.argv) == 1):
    print("Usage: gitupdate.py (PATH TO DIR OF GIT REPOS)")
    exit()
directory = sys.argv[1]
files = os.listdir(directory)
os.chdir(directory)

for f in files:
    if f[0] != '.':
        if os.path.isdir(f):
            os.chdir(f)
            if os.path.isdir(".git"):
                cmd = "git pull"
                os.system(cmd)
                os.chdir("../")
            else:
                os.chdir("../")


