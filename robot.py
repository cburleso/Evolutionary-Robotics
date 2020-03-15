import math
import random
import constants as c
class ROBOT:
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)
        del self.O, self.J, self.S, self.SN, self.MN

    def send_objects(self, sim):
        self.O0 = sim.send_box(position = (0, 0, c.L + c.R), sides = (c.L, c.L, 2 * c.R), color = (0.5, 0.5, 0.5))
        self.O1 = sim.send_cylinder((0, c.L, c.L + c.R), length = c.L, radius = c.R, color = (1, 0, 0), orientation = (0, 1, 0))
        self.O2 = sim.send_cylinder((c.L, 0, c.L + c.R), length = c.L, radius = c.R, color = (0, 1, 0), orientation = (1, 0, 0))
        self.O3 = sim.send_cylinder((0, -c.L, c.L + c.R), length = c.L, radius = c.R, color = (0, 0, 1), orientation = (0, -1, 0))
        self.O4 = sim.send_cylinder((-c.L, 0, c.L + c.R), length = c.L, radius = c.R, color = (0.5, 0, 0.5), orientation = (-1, 0, 0))
        self.O5 = sim.send_cylinder((0, c.L*3/2, c.L/2 + c.R), length = c.L, radius = c.R, color = (1, 0, 0))
        self.O6 = sim.send_cylinder((c.L*3/2, 0, c.L/2 + c.R), length = c.L, radius = c.R, color = (0, 1, 0.5))
        self.O7 = sim.send_cylinder((0, -c.L*3/2, c.L/2 + c.R), length = c.L, radius = c.R, color = (0, 0, 1))
        self.O8 = sim.send_cylinder((-c.L*3/2, 0, c.L/2 + c.R), length = c.L, radius = c.R, color = (0.5, 0, 0.5))

        self.O = {}
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8


    def send_joints(self, sim):
        self.J0 = sim.send_hinge_joint(self.O0, self.O1, (0, c.L/2, c.L + c.R), axis = (-1, 0, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J1 = sim.send_hinge_joint(self.O1, self.O5, (0, c.L*3/2, c.L + c.R), axis = (-1, 0, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J2 = sim.send_hinge_joint(self.O0, self.O2, (c.L/2, 0, c.L + c.R), axis = (0, -1, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J3 = sim.send_hinge_joint(self.O2, self.O6, (c.L*3/2, 0, c.L + c.R), axis = (0, -1, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J4 = sim.send_hinge_joint(self.O0, self.O3, (0, -c.L/2, c.L + c.R), axis = (1, 0, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J5 = sim.send_hinge_joint(self.O3, self.O7, (0, -c.L*3/2, c.L + c.R), axis = (1, 0, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J6 = sim.send_hinge_joint(self.O0, self.O4, (-c.L/2, 0, c.L + c.R), axis = (0, 1, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))
        self.J7 = sim.send_hinge_joint(self.O4, self.O8, (-c.L*3/2, 0, c.L + c.R), axis = (0, 1, 0), joint_range = (-3.14159 / 2, 3.14159 / 2))

        self.J = {}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7

    def send_sensors(self, sim):
        self.T0 = sim.send_touch_sensor(body_id = self.O5)
        self.T1 = sim.send_touch_sensor(body_id = self.O6)
        self.T2 = sim.send_touch_sensor(body_id = self.O7)
        self.T3 = sim.send_touch_sensor(body_id = self.O8)

        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3
        

        self.yPos = sim.send_position_sensor(body_id = self.O0, which_dimension = 'y') # Used when calculating fitness
        
        #self.P2 = sim.send_proprioceptive_sensor(joint_id = joint)

        #R3_1 = sim.send_ray(redObject, (0, 1.1, 1.1), (0, 1, 0))
        #self.R3_2 = sim.send_ray_sensor(R3_1)


    def send_neurons(self, sim):
        self.SN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
            
        self.MN = {}
        for j in self.J:
            newMN = sim.send_rotary_actuator(joint_id = self.J[j])
            self.MN[j] = sim.send_motor_neuron(newMN) #, tau = 0.3)
            

    def send_synapses(self, sim, wts):
        # connect each sensor neuron to each motor neuron within robot
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id = self.SN[j], target_neuron_id = self.MN[i], weight = wts[j, i])

    
                
    



