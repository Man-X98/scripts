#!/bin/bash

# Script builds markdown files in directory using pandoc

# IMPORTANT
# Pandoc has to be installed 

# TODO
# Check if markdown file was modified AFTER creation of PDF file
# Only recompile if markdown file is newer than PDF file
# Saves time in directory with a large number of markdown files
# https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times


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
        command = "pandoc -f markdown-implicit_figures -t pdf {} -o {}".format(file, filename)
        subprocess.call(command, cwd=path, shell=True)# , executable="/bin/zsh")
        buildFiles.append("File Build: {} --> {}".format(file, filename))
        print(buildFiles[-1])

print("Finished building markdown files in directory: {}".format(path))


