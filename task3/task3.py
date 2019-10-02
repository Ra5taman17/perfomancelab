from sys import argv
import os

db = [0 for i in range(16)]
if __name__ == "__main__":
    files = os.listdir(argv[1])
    for i in range(len(files)):
        with open(os.path.join(argv[1], files[i])) as file:
            n = 0
            for line in file.readlines():
                db[n] += float(line.rstrip())
                n += 1
    print(db.index(max(db))+1)