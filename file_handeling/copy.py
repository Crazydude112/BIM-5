try:
    with open("file.txt","r") as source:
        with open("file2.txt","a") as destination:
            for line in source:
                destination.write(line)
            print("The file has been copied successfully.")
except FileNotFoundError:
    print("The source file does not exist.")
file=open("file2.txt","r")
print(file.readlines())
file.close()
