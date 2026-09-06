# Write data to a new file with line breaks

with open("dataset_ready/viwik18.txt", "r") as f:
    file = f.read()

with open("dataset_ready/viwik18_lineSentences.txt", "w") as f1:
    start = 0
    for i in range(len(file)-1):
        if file[i:i+2] == "  ":
            f1.write(file[start:i] + "\n")
            start = i + 2
    f1.write(file[start:])
