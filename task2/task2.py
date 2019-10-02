from sys import argv

coords = []
figure = []

def check(x, y):
    for i in range(len(figure)):
        if x == figure[i][0] and y == figure[i][1]:
            return 0
    for i in range(len(figure)):
        if (x == figure[i][0] and (y < max(figure[1][1], figure[3][1]) and y > min(figure[1][1], figure[3][1]))) or (y == figure[i][1] and (x < max(figure[0][0], figure[2][0]) and x > min(figure[0][0], figure[2][0]))):
            return 1
    if (x < max(figure[0][0], figure[2][0]) and x > min(figure[0][0], figure[2][0])) and (y < max(figure[1][1], figure[3][1]) and y > min(figure[1][1], figure[3][1])):
        return 2
    else:
        return 3


if __name__ == "__main__":
    with open(argv[1]) as file:
        for line in file.readlines():
            figure.append(line.rstrip().split(' '))
    with open(argv[2]) as file:
        for line in file.readlines():
            coords.append(line.rstrip().split(' '))
    for i in range(len(coords)):
        print(check(coords[i][0], coords[i][1]))