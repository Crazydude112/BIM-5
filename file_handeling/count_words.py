with open("file.txt", "r") as file:
    count = 0

    for line in file:
        count += len(line.split())

    print("Total words:", count)