#!/bin/bash

# Script builds markdown files in directory unsing pandoc

# IMPORTANT
# Needs explicit path to pandoc executable

import os
import sys
import subprocess

path = os.getcwd()
pandocPath = "/home/johannes/Downloads/pandoc-3.1/bin/pandoc"

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
        command = "{} {} -o {}".format(pandocPath, file, filename)
        subprocess.call(command, cwd=path, shell=True, executable="/bin/zsh")
        buildFiles.append("File Build: {} --> {}".format(file, filename))
        print(buildFiles[-1])

print("Finished building markdown files in directory: {}".format(path))


