from robot import ROBOT
import pyrosim
import matplotlib.pyplot as plt
import random

for i in range(0, 10):
    sim = pyrosim.Simulator(play_paused = False, eval_steps = 500)
    sim.set_camera((-3, -3, 2), (45, -15, 0), tracking = 'none', body_to_track = 0)
    #et_camera(xyz, hpr, tracking='none', body_to_track=0)
    robot = ROBOT(sim, random.random() * 2 - 1)
    sim.start()
    sim.wait_to_finish()

# Sensor data from red cylinder
#sensorData = sim.get_sensor_data(sensor_id = P2)
#print(sensorData)

# Plot of sensor data
#f = plt.figure()
#panel = f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-1, +2)

#plt.show()
