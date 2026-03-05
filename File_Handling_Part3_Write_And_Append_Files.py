# ------------------------------------------------
# -- File Handling Part3 Write And Append Files --
# ------------------------------------------------
# myFile = open(r"C:\Users\ahmad\Desktop\Python-project\ahmad.txt", "w")
# myFile.write("Hello From Python File\n ")
# myFile.write("Second Line ")
# myFile = open(r"C:\Users\ahmad\Desktop\Python-project\fun.txt", "w")
# myFile.write("Hello World\n" * 1000)
# myList = ["Ahmad\n", "Ali\n", "Osama\n"]
# myFile = open(r"C:\Users\ahmad\Desktop\Python-project\ahmad.txt", "w")
# myFile.writelines(myList)
myFile = open(r"C:\Users\ahmad\Desktop\Python-project\ahmad.txt", "a")
myFile.writelines("Hello World\n")
myFile.writelines("This is another line")
myFile.writelines("Testing Position \n\n\n\n ")
myFile.writelines("ahmad")
myFile.close()
