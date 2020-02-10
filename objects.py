
import pyrosim

sim = pyrosim.Simulator(play_paused = True, eval_steps = 1000)

# (x, y, z) tuple used within send_cylinder
whiteObject = sim.send_cylinder((0, 0, 0.6), length = 1.0, radius = 0.1)
redObject = sim.send_cylinder((0, 0.5, 1.1), length = 1.0, radius = 0.1, color = (1, 0, 0), orientation = (0, 1, 0))

sim.start()
sim.wait_to_finish()

