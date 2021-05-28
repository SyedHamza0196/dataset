import os

files = os.listdir("/home/hamza/MEGA/new/allTrain/labels/")
# print(files)
for file in files:
    with open("/home/hamza/MEGA/new/allTrain/labels/"+file, "r") as f:
        lines = f.readlines() #reads one line at a time
    with open("/home/hamza/MEGA/new/allTrain/labels/"+file, "w") as f:
        for line in lines:
            if line.split()[0] == "0":
                f.write(line)
            if line.split()[0] == "2":
                x = line.replace("2","0",1)
                f.write(x)
            if line.split()[0] == "None":
                x = line.replace("None","0",1)
                f.write(x)