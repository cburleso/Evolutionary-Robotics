import pyrosim
import random
import math
import numpy
from robot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = numpy.random.random(4) * 2 - 1
        self.fitness = 0
        

##    def Evaluate(self, pb):
##        sim = pyrosim.Simulator(play_paused = False, eval_steps = 300, play_blind = pb)
##        sim.set_camera((-4, -1, 2), (15, -15, 0), tracking = 'none', body_to_track = 0)
##        robot = ROBOT(sim, self.genome)
##
##        sim.start()
##        sim.wait_to_finish()

##        yPos = sim.get_sensor_data(sensor_id = robot.y)
##        
##        self.fitness = yPos[-1]

    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(play_paused = False, eval_steps = 300, play_blind = pb)
        self.sim.set_camera((-4, -1, 2), (15, -15, 0), tracking = 'none', body_to_track = 0)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        yPos = self.sim.get_sensor_data(sensor_id = self.robot.y)
        self.fitness = yPos[-1]
        del self.sim
        
    def Mutate(self):
        geneToMutate = random.randint(0, 3)
        self.genome[geneToMutate] = random.gauss(self.genome[geneToMutate], math.fabs(self.genome[geneToMutate]))

    def Print(self):
        print('[', self.ID, self.fitness, '] ', end = '')

