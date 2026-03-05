# ----------------------------
# -- File Handling Part One --
# ----------------------------
# "a" Append : Open File For Appending Values , Create File If Not Exists
# "r" Read   : [Default Value] Open File For Read And Give Error If File Is Not Exists
# "w" Write  :  Open File For Working , Create File If Not exists
# "x" Create :  Create File, Give Error If File Exists
# ----------------------------

# import os

# Main Current Working Directory
# print(os.getcwd())
# Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__)))
# Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())
# print(os.path.abspath(__file__))
file = open(r"C:\Users\ahmad\Desktop\Python-project\ahmad.txt")
# file = open("C:\Users\ahmad\Desktop\\nPython-project\ahmad.txt")
