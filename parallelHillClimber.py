from population import POPULATION
import copy

parents = POPULATION(10)
parents.Evaluate(False, True)
parents.Print()

print()

for g in range(1, 201):
    children = copy.deepcopy(parents)
    children.Mutate()
    children.Evaluate(False, True)
    parents.ReplaceWith(children)
    print(g, end = ' ')
    parents.Print()
    print()
    
parents.Evaluate(True, False)

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
