with open("file2.txt", "r") as file:
    lines = words = chars = 0

    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)