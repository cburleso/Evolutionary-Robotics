from individual import INDIVIDUAL
import pickle

f = open('robot.p', 'rb')
best = pickle.load(f) # best individual instance (based on fitness)
f.close()

# draw best individual to screen
best.Evaluate(False)
print('Best Fitness:', best.fitness)
