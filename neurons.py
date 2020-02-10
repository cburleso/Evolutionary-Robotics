
import pyrosim
import matplotlib.pyplot as plt

sim = pyrosim.Simulator(play_paused = True, eval_steps = 100)

# Red and white cylinders
whiteObject = sim.send_cylinder((0, 0, 0.6), length = 1.0, radius = 0.1)
redObject = sim.send_cylinder((0, 0.5, 1.1), length = 1.0, radius = 0.1, color = (1, 0, 0), orientation = (0, 1, 0))

# Joint to connect red and white cylinder
joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.1), axis = (-1, 0, 0), joint_range = (-3.14159/2, 3.14159))

# Touch sensors for red and white cylinders
T0 = sim.send_touch_sensor(body_id = whiteObject)
T1 = sim.send_touch_sensor(body_id = redObject)

# Proprioceptive sensor for cylinder joint
P2 = sim.send_proprioceptive_sensor(joint_id = joint)

# Ray sensor for red object
R3_1 = sim.send_ray(redObject, (0, 1.1, 1.1), (0, 1, 0))
R3_2 = sim.send_ray_sensor(R3_1)

# Sensor neurons for white and red cylinder touch sensors
SN0 = sim.send_sensor_neuron(sensor_id = T0)
SN1 = sim.send_sensor_neuron(sensor_id = T1)

# Motor neuron for cylinder joint
MN2 = sim.send_rotary_actuator(joint_id = joint)


sim.start()
sim.wait_to_finish()

# Sensor data from red cylinder
sensorData = sim.get_sensor_data(sensor_id = R3_2)
print(sensorData)

# Plot of sensor data
f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
#panel.set_ylim(-1, +2)

plt.show()
