from sys import argv
from numpy import median
from numpy import percentile

if __name__ == "__main__":
    db = []
    with open(argv[1]) as file:
        for line in file.readlines():
            db.append(int(line.rstrip()))
    print('%.2f' % percentile(db, 90), end='\n')
    print('%.2f' % median(db), end='\n')
    print('%.2f' % max(db), end='\n')
    print('%.2f' % min(db), end='\n')
    print('%.2f' % (sum(db)/len(db)), end='')