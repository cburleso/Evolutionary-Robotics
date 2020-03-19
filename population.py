from individual import INDIVIDUAL
import constants as c
import copy
import random

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        self.popSize = popSize

    def Winner_Of_Tournament_Selection(other):
        p1 = random.randint(0, other.popSize - 1)
        p2 = random.randint(0, other.popSize - 1)
        while (p2 == p1):
            p2 = random.randint(0, other.popSize - 1)

        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        else:
            return other.p[p2]
        
    def Fill_From(self, other):
        self.Copy_Best_From(other)
        self.Collect_Children_From(other)

    def Collect_Children_From(self, other):
        for i in range(1, len(other.p)):
            winner = other.Winner_Of_Tournament_Selection()
            self.p[i] = copy.deepcopy(winner)
            self.p[i].Mutate()
            
    def Copy_Best_From(self, other):
        best = 0
        for i in other.p:
            if other.p[i].fitness > other.p[best].fitness:
                best = i
        bestInd = copy.deepcopy(other.p[best])
        self.p[0] = bestInd
        
        
    def Initialize(self):
        for i in range(0, self.popSize):
            self.p[i] = INDIVIDUAL(i)
        
    def Print(self):
        for i in self.p:
            if i in self.p:
                self.p[i].Print()
        print()

    def Evaluate(self, envs, pp, pb):
        for e in range(c.numEnvs):
            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e], pp, pb)
            for i in self.p:
                self.p[i].Compute_Fitness()
            
        

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]
        
