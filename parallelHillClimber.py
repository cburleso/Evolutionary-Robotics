##from robot import ROBOT
##from individual import INDIVIDUAL
from population import POPULATION
import copy
##import pyrosim
##import matplotlib.pyplot as plt
##import random
##import copy
##import pickle
##
##parent = INDIVIDUAL()
##parent.Evaluate(True)
##print(parent.fitness)
##
##for i in range(0, 100):
##    child = copy.deepcopy(parent)
##    child.Mutate()
##    child.Evaluate(True)
##    print('[g:', i + 1, ']', '[pw:', parent.genome, ']', '[p:', parent.fitness , ']', '[c:', child.fitness, ']')
##    if (child.fitness > parent.fitness):
##        parent = child
##        child.Evaluate(True)
##        # f = open('robot.p', 'wb')
##        # pickle.dump(parent, f)
##        # f.close()

parents = POPULATION(5)
parents.Evaluate()
parents.Print()

print()

for g in range(1, 101):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate()
    parents.ReplaceWith(children)
    print(g, end = ' ')
    parents.Print()
    print()
    


'''    
 Sensor data from red cylinder
sensorData = sim.get_sensor_data(sensor_id = P2)
print(sensorData)

 Plot of sensor data
f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
panel.set_ylim(-1, +2)

plt.show()
'''
