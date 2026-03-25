# --------------------------------
# -- File Handling => Read File --
# --------------------------------
myFile = open(r"C:\Users\ahmad\Desktop\Python-project\ahmad.txt", "r")
# print(myFile)  # File Data Object
# print(type(myFile))
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)
# print(myFile.read())
# print(myFile.read(5))
# print(myFile.readline(10))
# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readlines(50))
# print(myFile.readlines())
# print(type(myFile.readlines()))
for line in myFile:
    print(line)
    if line.startswith("07"):
        break
myFile.close()
