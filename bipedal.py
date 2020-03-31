import sys
sys.path.insert(1, '/home/cburleso/Desktop/pyrosim-master')
import pyrosim
import numpy

maxDistance = 0
for i in range(10):
    # create simulator 
    sim = pyrosim.Simulator(play_paused = False, eval_steps = 1000, play_blind = False)
    sim.set_camera((-4, -1, 2), (15, -15, 0), tracking = 'none', body_to_track = 0)

    # bipedal hip box
    hip = sim.send_box(position = (0, 0, 0.45), sides = (0.25, 0.05, 0.05), color = (0, 0, 1))
    
    # femurs
    rFemur = sim.send_cylinder((0.125, 0, 0.35), length = 0.2, radius = 0.025, color = (1, 0, 0))# orientation = (0, 0, 1))
    lFemur = sim.send_cylinder((-0.125, 0, 0.35), length = 0.2, radius = 0.025, color = (1, 0, 0))#, orientation = (0, 0, 1))

    # shins 
    rShin = sim.send_cylinder((0.125, 0, 0.125), length = 0.2, radius = 0.025, color = (0, 1, 0))#, orientation = (0, 0, 1))
    lShin = sim.send_cylinder((-0.125, 0, 0.125), length = 0.2, radius = 0.025, color = (0, 1, 0))#, orientation = (0, 0, 1))

    # feet
    rFoot = sim.send_box(position = (0.125, 0.03, 0.015), sides = (0.075, 0.12, 0.03), color = (0, 0, 0))
    lFoot = sim.send_box(position = (-0.125, 0.03, 0.015), sides = (0.075, 0.12, 0.03), color = (0, 0, 0))

    O = {}
    O[0] = hip
    O[1] = rFemur
    O[2] = lFemur
    O[3] = rShin
    O[4] = lShin
    O[5] = rFoot
    O[6] = lFoot

    # femur/hip joints
    rFemurHip = sim.send_hinge_joint(hip, rFemur, (0.125, 0, 0.45), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))
    lFemurHip = sim.send_hinge_joint(hip, lFemur, (-0.125, 0, 0.45), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))

    # femur/shin joints
    rFemurShin = sim.send_hinge_joint(rFemur, rShin, (0.125, 0, 0.25), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))
    lFemurShin = sim.send_hinge_joint(lFemur, lShin, (-0.125, 0, 0.25), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))

    # ankle joints
    rAnkle = sim.send_hinge_joint(rShin, rFoot, (0.125, 0, 0), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))
    lAnkle = sim.send_hinge_joint(lShin, lFoot, (-0.125, 0, 0), axis = (-1, 0, 0), joint_range = (-3.14159 / 4, 3.14159 / 4))

    J = {}
    J[0] = rFemurHip
    J[1] = lFemurHip
    J[2] = rFemurShin
    J[3] = lFemurShin
    J[4] = rAnkle
    J[5] = lAnkle

    # touch sensors for feet
    rFootSensor = sim.send_touch_sensor(body_id = rFoot)
    lFootSensor = sim.send_touch_sensor(body_id = lFoot)

    # proprioceptive sensors for each joint
    P1 = sim.send_proprioceptive_sensor(joint_id = rFemurHip)
    P2 = sim.send_proprioceptive_sensor(joint_id = lFemurHip)
    P3 = sim.send_proprioceptive_sensor(joint_id = rFemurShin)
    P4 = sim.send_proprioceptive_sensor(joint_id = lFemurShin)
    P5 = sim.send_proprioceptive_sensor(joint_id = rAnkle)
    P6 = sim.send_proprioceptive_sensor(joint_id = lAnkle)

    # position sensor for calculating fitness value
    yPos = sim.send_position_sensor(body_id = hip, which_dimension = 'y')
    
    S = {}
    S[0] = rFootSensor
    S[1] = lFootSensor
    S[2] = P1
    S[3] = P2
    S[4] = P3
    S[5] = P4
    S[6] = P5
    S[7] = P6
    
    # sensor neurons for each touch sensor in foot
    SN = {}
    for s in S:
        SN[s] = sim.send_sensor_neuron(sensor_id = S[s])

    # motor neurons for joints
    MN = {}
    for j in J:
        newMN = sim.send_rotary_actuator(joint_id = J[j])
        MN[j] = sim.send_motor_neuron(newMN)#, tau = 0.6)

    # temporary random genome for robot
    wts = numpy.random.rand(8, 6) * 2 - 1

    # synapses for each sensor neuron to each motor neuron in biped
    for j in SN:
        for i in MN:
            sim.send_synapse(source_neuron_id = SN[j], target_neuron_id = MN[i], weight = wts[j, i])
            
    # start simulator 
    sim.start()
    sim.wait_to_finish()

    y = sim.get_sensor_data(sensor_id = yPos)
    try:
        distance = y[-1]
    except:
        distance = -1000
        
    if distance > maxDistance:
        maxDistance = distance

    print('Distance: ', distance)

print('Maximum Distance: ', maxDistance)
