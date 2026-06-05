with open("file2.txt","r") as f:
    word=input("enter the word to search:")
    if word in f.read():
        print(f"The word '{word}' is present in the file.")
    else:
        print(f"The word '{word}' is not present in the file.")
