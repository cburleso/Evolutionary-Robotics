import math
class ROBOT:
    def __init__(self, sim, wts):
        whiteObject = sim.send_cylinder((0, 0, 0.6), length = 1.0, radius = 0.1)
        redObject = sim.send_cylinder((0, 0.5, 1.1), length = 1.0, radius = 0.1, color = (1, 0, 0), orientation = (0, 1, 0))

        joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.1), axis = (-1, 0, 0), joint_range = math.pi)

        T0 = sim.send_touch_sensor(body_id = whiteObject)
        T1 = sim.send_touch_sensor(body_id = redObject)

        P2 = sim.send_proprioceptive_sensor(joint_id = joint)

        R3_1 = sim.send_ray(redObject, (0, 1.1, 1.1), (0, 1, 0))
        R3_2 = sim.send_ray_sensor(R3_1)

        # sensor neurons embedded in robot 
        SN0 = sim.send_sensor_neuron(sensor_id = T0)
        SN1 = sim.send_sensor_neuron(sensor_id = T1)
        SN2 = sim.send_sensor_neuron(sensor_id = P2)
        SN3 = sim.send_sensor_neuron(sensor_id = R3_2)

        # dictionary of sensor neurons 
        sensorNeurons = {}
        sensorNeurons[0] = SN0
        sensorNeurons[1] = SN1
        sensorNeurons[2] = SN2
        sensorNeurons[3] = SN3

        # motor neuron embedded in robot 
        MN2_1 = sim.send_rotary_actuator(joint_id = joint)
        MN2_2 = sim.send_motor_neuron(MN2_1)

        # dictionary of motor neurons
        motorNeurons = {}
        motorNeurons[0] = MN2_2

        # connect each sensor neuron to each motor neuron within robot 
        for s in sensorNeurons:
            for m in motorNeurons:
                sim.send_synapse(source_neuron_id = sensorNeurons[s], target_neuron_id = motorNeurons[m], weight = wts[s])
        


        self.x = sim.send_position_sensor(body_id = redObject, which_dimension = 'x')
        self.y = sim.send_position_sensor(body_id = redObject, which_dimension = 'y')
        self.z = sim.send_position_sensor(body_id = redObject, which_dimension = 'z')        
    



