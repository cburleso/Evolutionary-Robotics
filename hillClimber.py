from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import matplotlib.pyplot as plt
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(False)
print(parent.fitness)

for i in range(0, 100):
    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print('[g:', i + 1, ']', '[pw:', child.genome, ']', '[p:', parent.fitness , ']', '[c:', child.fitness, ']')
    if (child.fitness > parent.fitness):
        parent = child
        child.Evaluate(True)
        # f = open('robot.p', 'wb')
        # pickle.dump(parent, f)
        # f.close()

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
