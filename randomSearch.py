from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import matplotlib.pyplot as plt
import random

for i in range(0, 10):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)

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
