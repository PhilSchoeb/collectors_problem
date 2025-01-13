import math
import time

pmrDic = {}
vkDic = {}

class Pmr:
    def __init__(self, m, r):
        self.m = m
        self.r = r

    def __eq__(self, other):
        return self.m == other.m and self.r == other.r

    def __hash__(self):
        h = self.m.__hash__() + self.r.__hash__()
        return h


class Vk:
    def __init__(self, m, t, k):
        self.m = m
        self.t = t
        self.k = k

    def __eq__(self, other):
        return self.m == other.m and self.t == other.t and self.k == other.k

    def __hash__(self):
        h = self.m.__hash__() + self.t.__hash__() + self.k.__hash__()
        return h


def pmr(m, r):
    global pmrDic
    if m < r:
        return 0
    if r == 1:
        if m == 0:
            return 0
        else:
            return 1
    result = 0
    for i in range(1, m - r + 2):
        pmrKey = Pmr(m-i, r-1)
        if pmrDic.get(pmrKey):
            recursiveProb = pmrDic.get(pmrKey)
        else:
            recursiveProb = pmr(m-i, r-1)
            pmrDic.update({pmrKey: recursiveProb})
        result += recursiveProb * math.comb(m, i) * (1/r)**(i) * (1-1/r)**(m-i)
    return result

def vk(m, t, k):
    global vkDic
    if m < t:
        return 0
    if t == 0:
        return 1
    vkKey1 = Vk(m-1,t-1,k)
    vkKey2 = Vk(m-1,t,k)
    if vkDic.get(vkKey1):
        #print("its in")
        recursiveProb1 = vkDic.get(vkKey1)
    else:
        recursiveProb1 = vk(m-1, t-1, k)
        vkDic.update({vkKey1: recursiveProb1})
    if vkDic.get(vkKey2):
        recursiveProb2 = vkDic.get(vkKey2)
    else:
        recursiveProb2 = vk(m-1, t, k)
        vkDic.update({vkKey2: recursiveProb2})
    result = ((float(t)/k) * recursiveProb1) + (1-(float(t)/k)) * recursiveProb2
    return result

def C_under_51_pmr():
    for i in range(1, 51):
        probability = pmr(12*i, 32)
        numberItems = str(12 * i)
        print("With c = " + str(i) + ", we have " + numberItems + " items and 32 different "
              "types. p(" + str(i) + ") = " + str(probability))
    print("The probability of needing more than 50 boxes is : " + str(1 - probability))
    return probability

def C_under_51_vk():
    for i in range(1, 51):
        probability = vk(12*i, 32, 32)
        numberItems = str(12 * i)
        print("With c = " + str(i) + ", we have " + numberItems + " items and 32 different "
              "types. p(" + str(i) + ") = " + str(probability))
    print("The probability of needing more than 50 boxes is : " + str(1 - probability))
    return probability


time1 = time.time()
C_under_51_vk()
time2 = time.time()
C_under_51_pmr()
time3 = time.time()

print("VK : " + str(time2 - time1))
print("PMR : " + str(time3 - time2))
