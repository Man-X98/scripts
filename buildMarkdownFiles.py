#!/bin/bash

# Script builds markdown files in directory using pandoc

# IMPORTANT
# Pandoc has to be installed 

import os
import sys
import subprocess

path = os.getcwd()

try:
    userArgs = sys.argv[1]
    print("Directory submitted: {}".format(userArgs))
    path = path + "/{}".format(userArgs)
except IndexError:
    print("Building current directory")

files = os.listdir(path)
buildFiles = []
for file in files:
    if file[-3:] == ".md":
        # build File:
        filename = file[:-2] + "pdf"
        command = "pandoc {} -o {}".format(file, filename)
        subprocess.call(command, cwd=path, shell=True)# , executable="/bin/zsh")
        buildFiles.append("File Build: {} --> {}".format(file, filename))
        print(buildFiles[-1])

print("Finished building markdown files in directory: {}".format(path))


