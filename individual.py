import pyrosim
import random
import math
import numpy
import constants as c 
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = numpy.random.rand(4, 8) * 2 - 1
        self.fitness = 0
        
    def Start_Evaluation(self, env, pp, pb):
        self.sim = pyrosim.Simulator(play_paused = pp, eval_steps = c.evalTime, play_blind = pb)
        env.Send_To(self.sim)
        #self.sim.set_camera((-4, -1, 2), (15, -15, 0), tracking = 'none', body_to_track = 0)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data(sensor_id = self.robot.yPos)
        if (y == None):
            self.fitness = -1000
        else:
            self.fitness = y[-1]
        
        del self.sim
        del self.robot
        
    def Mutate(self):
        randRow = random.randint(0, 3)
        randCol = random.randint(0, 7)
        #self.genome[randRow][randCol] = random.gauss(self.genome[randRow][randCol], math.fabs(self.genome[randRow][randCol]))
        self.genome[randRow][randCol] = random.uniform(-1, 1)
        if (self.genome[randRow][randCol] > 1):
            self.genome[randRow][randCol] = 1
        if (self.genome[randRow][randCol] < -1):
            self.genome[randRow][randCol] = -1
    
    def Print(self):
        print('[', self.ID, self.fitness, '] ', end = '')

