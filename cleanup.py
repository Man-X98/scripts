import os
import sys



path=os.getcwd()

try:
    userArgs = sys.argv[1]
    print("Directory submitted: {}".format(userArgs))
    path = path + "/{}".format(userArgs)
except IndexError:
    print("Cleaning current directory")

bad_endings=['.log', '.aux', '.nav', '.out', '.snm', '.toc', '.vrb', 'x.gz']

removed_files=0
statement='{} files were delted'

files=os.listdir(path)
for filename in files:
	if filename[-4:] in bad_endings:
		os.remove(path + '/' + filename)
		removed_files = removed_files + 1
		print((path + '/' + filename + ' was removed'))
print("{} files were removed".format(removed_files))

