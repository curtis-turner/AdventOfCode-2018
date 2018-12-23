#chars to remove from string
charsToStrip = '[]'

#setting up my file for day 4 if i every get there lol
with open('day4p1-curtis-input.txt') as infile:
    data = [''.join(c for c in x if c not in charsToStrip) for x in infile.read().splitlines()]

#sort data by time inlcuding hour and minute
data.sort(key = lambda x : x.split(' ')[0] + ' ' + x.split(' ')[1])

#create dictionary to store gaurds times asleep. Format with be like this - {id: timeasleep}
guards = {}

start = 0
end = 0

#create gaurd id in dictionary with initial value of zero
for i in range(len(data)):
    if 'Guard' in data[i]:
        date = data[i].split(' ')[0]
        ID = data[i].split(' ')[3][1:]
        start = 0
        end = 0

    if 'asleep' in data[i]:
        start = data[i].split(' ')[1].split(':')[1]

    if 'wakes' in data[i]:
        end = data[i].split(' ')[1].split(':')[1]

    if start != 0 and end != 0:
        timeAsleep = int(end) - int(start)
        if date in guards.keys():
            if ID in guards[date].keys():
                guards[date][ID] += [i for i in range(int(start), int(end))]
                #timeAsleep
        else:
            guards[date] = {ID:[i for i in range(int(start), int(end))]}#timeAsleep
        start = 0
        end = 0
        

d = max(guards.keys(), key=(lambda key: guards[key]))

print(guards[d])
m = 0
for i in guards.keys():
    for j in guards[i].keys():
        #print(len(guards[i][j]))
        if len(guards[i][j]) > m:
            m = len(guards[i][j])

print(m)

'''
if any(gaurd for gaurd in gaurds if gaurd['id'] == gaurdID):
            gaurd = next(gaurd for gaurd in gaurds if gaurd['id'] == gaurdID)
        else:
            gaurd = {'date': i.split(' ')[0] + ' ' + i.split(' ')[1], 'id': gaurdID, 'asleep': 0}
            gaurds.append(gaurd)

print(newdata)

gaurds = [{'date': '11-01', 'id': '#123' , 'minutes': 0}]

def countOfMinutesAwake(id, data):
    totalMinutesAwake = 0
    for i in data:
        if id in i:
            print('Id is in this line of the data...')
    
    return totalMinutesAwake


for i in newdata:
    print(i)
    if 'Gaurd' in i:
        gaurdNum = i.split(' ')[2]
        print(gaurdNum)
        if gaurdNum not in gaurds:
            gaurds[gaurdNum] = 0
        else:
            gaurds[gaurdNum] = countOfMinutesAwake(gaurdNum, newdata)

with open('check-data.txt', 'w') as outfile:
    for i in newdata:
        outfile.write(i + '\n')

Notes in the Comment
addtime = map(lambda l : l[0].split(' ')[0] + ' ' + l[0].split(' ')[1], data)
print(list(addtime))
print(data[0])


newdata =[]
for i in range(len(data)):
    temp = ''
    string = data[i]
    timestamp = string.split(' ')[0] + ' ' + string.split(' ')[1]
    timestamp = timestamp[1:-1]
    timestap = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    temp += timestamp + ' ' + data[i]
    newdata.append(temp)

#print(newdata[0])

with open('check-data-3.txt', 'w') as outfile:
    for i in data:
        outfile.write(i + '\n')
'''

