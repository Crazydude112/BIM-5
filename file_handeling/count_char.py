with open("file2.txt","r") as file:
    # lines=file.read()
    # print(lines.strip())
    count=0
    for line in file:
        for ch in line:
            if ch ==" ":
                count+=1
    print(count)