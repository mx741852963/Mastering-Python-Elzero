# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
the_file = None
the_tries = 5
while the_tries > 0:
    try:  # try to open the file
        print("Enter The File Name With Absolute Path")
        print(f"{the_tries} tries left")
        print("Example :D:\\python\\File\\your-file.extension")
        file_name_and_path = input("Enter The File Name => :").strip()
        the_file = open(file_name_and_path, "r")
        print(the_file.read())
        break
    except FileNotFoundError:
        print("File Not Found")
        the_tries -= 1
    except:
        print("Something Went Wrong")
    finally:
        if the_file is not None:
            the_file.close()
            print("End of the File")
else:
    print("All Tries is done ")
