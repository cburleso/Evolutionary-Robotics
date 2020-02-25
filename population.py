from individual import INDIVIDUAL

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        for i in range(0, popSize):
            self.p[i] = INDIVIDUAL()

    def Print(self):
        for i in self.p:
            self.p[i].Print()

    def Evaluate(self):
        for i in self.p:
            self.p[i].Start_Evaluation(False)
            #self.p[i].Compute_Fitness()
