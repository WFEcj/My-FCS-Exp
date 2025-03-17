import datetime
file_name = "./DstrongTracking_400.txt"
file_result = "./DstrongTracking_400STRes.txt"
fo = open(file_name)
nodes = set()
#edges = []
lines = fo.readlines()
for line in lines:
    node = line.split( )
    nodes.update(node)
    #node.sort()
    #if node not in edges:
    #    edges.append(node)
print(len(nodes))
#print(len(edges))
fo.close()

def calF2(freVector):
    F_2 = 0
    for i in freVector.values():
        F_2 += i**2
    return F_2


oldStream = []
# newStream = []
# distinctElement = set()
triangleCount = 0
freVector = {}
F_1 = 0
print(datetime.datetime.today())
fo = open(file_name)
# for i in range(4) :
#    fo.readline()
lines = fo.readlines()
for line in lines:
    node = line.split()
    node.sort()
    if node not in oldStream:
        oldStream.append(node)
        for i in nodes:
            if i in node:
                continue
            F_1 += 1
            newlist = node[:]
            newlist.append(str(i))
            newlist.sort()

            strTemp = ",".join(newlist)
            # print(strTemp)
            if strTemp.strip() not in freVector.keys():
                freVector[strTemp] = 1
            else:
                freVector[strTemp] += 1
            # newStream.append(strTemp)
            # distinctElement.add(strTemp)
    #             if (F_1 % 50) == 0:
    #                 with open(file_result,'a',encoding='UTF-8') as f:
    #                     F_2 = calF2(freVector)
    #                     F_0 = len(freVector)
    #                     triangleCount = F_0 - 1.5 * F_1 + 0.5 * F_2
    #                     f.write(str(triangleCount))
    #                     f.write("\n")
    #     with open(file_result,'a',encoding='UTF-8') as f:
    #         F_2 = calF2(freVector)
    #         F_0 = len(freVector)
    #         triangleCount = F_0 - 1.5 * F_1 + 0.5 * F_2
    #         f.write(str(triangleCount))
    #         f.write("\n")
    F_2 = calF2(freVector)
    F_0 = len(freVector)
    triangleCount = F_0 - 1.5 * F_1 + 0.5 * F_2
    with open(file_result, 'a', encoding='UTF-8') as f:
        f.write(str(triangleCount))
        f.write("\n")
    line = fo.readline()

F_2 = calF2(freVector)
F_0 = len(freVector)
triangleCount = F_0 - 1.5 * F_1 + 0.5 * F_2
print(triangleCount)
print(datetime.datetime.today())
fo.close()