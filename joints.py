
import pyrosim

sim = pyrosim.Simulator(play_paused = True, eval_steps = 1000)

# White cylinder body
whiteObject = sim.send_cylinder((0, 0, 0.6), length = 1.0, radius = 0.1)

# Red cylinder body
redObject = sim.send_cylinder((0, 0.5, 1.1), length = 1.0, radius = 0.1, color = (1, 0, 0), orientation = (0, 1, 0))

# Joint to connect red and white cylinder
joint = sim.send_hinge_joint(whiteObject, redObject, (0, 0, 1.1), axis = (1, 0, 0), joint_range = (-3.14159/2, 3.14159))

sim.start()
sim.wait_to_finish()

