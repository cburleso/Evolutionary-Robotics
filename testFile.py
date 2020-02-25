import random
import math
for i in range(50):
    #print(random.random()*2 - 1)
    print(random.gauss(random.random()*2 - 1, math.fabs(random.random()*2 - 1)))
