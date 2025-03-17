import numpy as np
import random
import math
import datetime

class SampleTriangle:
    def __init__(self, n):
        self.a = -1
        self.b = -1
        self.v = -1
        self.x = False
        self.y = False
        self.beta = 0
        self.n = n  # number of vertices

    def update(self, u, w):
        self.a = u
        self.b = w

        temp = np.random.randint(1, self.n + 1)
        while temp == self.a or temp == self.b:
            temp = np.random.randint(1, self.n + 1)
        self.v = temp

        self.x = False
        self.y = False

    def check_triangle(self, u, w):
        if (self.a == u and self.v == w) or (self.a == w and self.v == u):
            self.x = True
        if (self.b == u and self.v == w) or (self.b == w and self.v == u):
            self.y = True

    def get_beta(self):
        if self.x and self.y:
            self.beta = 1
        else:
            self.beta = 0
        return self.beta

def getMaxMT(file_name1, file_name2):
    res = 0
    fo1 = open(file_name1)
    fo2 = open(file_name2)
    edges = fo1.readlines()
    numberTriangle = fo2.readlines()
    # print(len(edges))
    # print(len(numberTriangle))
    for i in range(len(edges)):
        if numberTriangle[i].strip() == "0.0":
            continue
        res = max(res, math.ceil((i + 1) / float(numberTriangle[i].strip())))
    fo1.close()
    fo2.close()
    return res



def getRes(m, rho):
    average = 0
    # for i in range(5):
    beta = 0
    querySet = random.sample(s_index, min(factor * math.ceil(m * n_total / 2 ** rho), len(s_index)))
    for alg in querySet:
        beta += S[alg].get_beta()
    T = beta / len(querySet) * m * (n_total - 2)
    average += T
    # average /= 5
    return average

def fed2S(edge, m):
    for alg in S:
        if np.random.randint(1, m + 1) == 1:
            alg.update(int(edge[0]), int(edge[1]))
        alg.check_triangle(int(edge[0]),int(edge[1]))

def Alg(file_name1, file_name2):
    rho = 0
    res = []
    fo1 = open(file_name1)
    fo2 = open(file_name2)
    fo3 = open(save_name, 'w')
    edges = fo1.readlines()
    numberTriangle = fo2.readlines()
    for i in range(len(edges)):
        edge = edges[i].strip().split( )
        fed2S(edge, i + 1)
        if numberTriangle[i].strip() == "0.0":
            # res.append(0)
            # fo3.write('0\n')
            continue
        print(i)
        if i < 5000:
            continue
        response = getRes(i + 1, rho)
        if response > 2**(rho + 1):
            rho = math.floor(math.log2(response))
            # response = getRes(i + 1, rho)
        # res.append(response)
        fo3.write(str(response) + '\n')
        print(str(i) + " " + str(response))
        # print(f"{i} {response}")
    fo1.close()
    fo2.close()
    return res

def saveResult(save_name, res):
    fo = open(save_name, 'w')
    for i in res:
        fo.write(str(i) + '\n')
    fo.close()

file_name1 = "./strongTracking.txt"
file_name2 = "./strongTrackingSTRes.txt"
save_name = "./strongTrackingOurAlg2.txt"

n_total = 200
epsilon = 0.1
delta = 0.01
# mtMax = getMaxMT(file_name1,file_name2)
# print(mtMax)
factor = math.ceil( 3 / epsilon**2 * math.log(2 / delta, math.e))
print(factor)
s = int(factor * (n_total - 2) * 0.5)
print(s)
s_index = list(x for x in range(s))

S = []
for i in range(s):
    S.append(SampleTriangle(n_total))

print(datetime.datetime.today())
Alg(file_name1, file_name2)
print(datetime.datetime.today())
