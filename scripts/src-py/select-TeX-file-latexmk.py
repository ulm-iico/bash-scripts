import numpy as np
import os
import sys
from tabulate import tabulate

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

path = sys.argv[1]
count = 0
listfilestable = []
listfiles = []

for i in sorted(os.listdir(path)):
    if i.endswith('.tex'):
        listfilestable.append([count, i])
        listfiles.append(i)
        count += 1

columns = ["No. File", "File Name"]
print(tabulate(listfilestable, headers=columns, numalign="center", tablefmt="orgtbl"))

while True:
    sfile = input(style.GREEN + "\nSelect TeX file to compile (number): ")
    try:
        sfile = int(sfile)
        fileselect = listfiles[sfile]
    except ValueError:
        print(style.RED + '¡Error! You should input a correct number! 😡')
        continue
    except IndexError:
        print(style.RED + '¡Error! You should input a correct number! 😡')
        continue
    else:
        print(style.GREEN + "You select: %s 😄" % (fileselect))
        break

diroutput = sys.argv[2]
type = sys.argv[3]

# Ensure the output directory exists
if not os.path.exists(diroutput):
    os.makedirs(diroutput)

latexmk_commands = {
    'lualatex': f"latexmk -lualatex -auxdir={diroutput} -outdir={diroutput} {fileselect}",
    'xelatex': f"latexmk -xelatex -pdf -e '$max_repeat=2' -g -f -shell-escape -auxdir={diroutput} -outdir={diroutput} {fileselect}",
    'figure': f"latexmk -shell-escape -pdflatex -pdf -g -e '$max_repeat=0' -f -auxdir={diroutput} -outdir={diroutput} {fileselect}",
    'general': f"latexmk -auxdir={diroutput} -bibtex -pdf -g -f -shell-escape -outdir={diroutput} {fileselect}",
    'revtex': f"latexmk -auxdir={diroutput} -bibtex -pdf -g -shell-escape -outdir={diroutput} {fileselect}",
    'asy': f"latexmk -pdf -g -f -auxdir={diroutput} -outdir={diroutput} {fileselect}",
}

# Default command if the type is not recognized
command = latexmk_commands.get(type, f"latexmk -auxdir={diroutput} -bibtex -pdf -g -f  -shell-escape -outdir={diroutput} {fileselect}")

# Run the command
os.system(command)