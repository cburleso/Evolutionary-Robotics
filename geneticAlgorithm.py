from population import POPULATION
import copy

parents = POPULATION(10)
parents.Initialize()
parents.Evaluate(False, True)
print('P', end = ' ')
parents.Print()

for g in range(1, 10):
    children = POPULATION(10)
    children.Fill_From(parents)
    children.Evaluate(False, True)
    print(g, end = ' ')
    children.Print()
    parents.ReplaceWith(children)

children.p[0].Start_Evaluation(True, False)


