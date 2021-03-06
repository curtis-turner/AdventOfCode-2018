#create fabric
fabric = [['0' for i in range(1000)]for j in range(1000)]

#read data from file or supply test input to list of claims
#claims = ["#1 @ 10,30: 40x40", "#2 @ 30,10: 40x40", "#3 @ 50,50: 20x20"]
with open('day3p1-curtis-input.txt') as infile:
    claims = infile.read().splitlines()

#area of overlapping fabric
overlap = 0

for i in claims:
    temp = i.split(' ')
    ID = temp[0][1:]
    x = int(temp[2].split(',')[0])
    y = int(temp[2].split(',')[1][:-1])
    width = int(temp[3].split('x')[0])
    height = int(temp[3].split('x')[1])

    #print statement for debugging
    #print('x: ' + str(x) + ', y: ' + str(y) + ', width: ' + str(width) + ', height: ' + str(height))

    for i in range(width):
        for j in range(height):
            if fabric[y+j][x+i] == '0':
                fabric[y+j][x+i] = '1'
            elif fabric[y+j][x+i] == '1':
                fabric[y+j][x+i] = 'x'
                overlap += 1

print(overlap)