from environments import ENVIRONMENTS
from population import POPULATION
import constants as c

envs = ENVIRONMENTS()



##import copy
##
parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, False, False)
##print('P', end = ' ')
##parents.Print()
##
##for g in range(1, c.numGens + 1):
##    children = POPULATION(c.popSize)
##    children.Fill_From(parents)
##    children.Evaluate(False, True)
##    print(g, end = ' ')
##    children.Print()
##    parents.ReplaceWith(children)
##
##children.p[0].Start_Evaluation(True, False)


