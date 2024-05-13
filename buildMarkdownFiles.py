#!/bin/bash
import os
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
        filename = file[:-2] + "pdf"
        # Check if PDF is up to date with markdown
        if filename in files:
            timePDF = os.path.getmtime(path + "/" + filename)
            timeMarkdown = os.path.getmtime(path + "/" + file)
            if timePDF > timeMarkdown:
                # skip compilation if markdown is up to date
                print("PDF for {} is up to date. Skipping compilation".format(filename))
                continue

        # Compile markdown file
        command = "pandoc -f markdown-implicit_figures -t pdf {} -o {}".format(file, filename)
        subprocess.call(command, cwd=path, shell=True)# , executable="/bin/zsh")
        buildFiles.append("File Build: {} --> {}".format(file, filename))
        print(buildFiles[-1])

print("Finished building markdown files in directory: {}".format(path))


