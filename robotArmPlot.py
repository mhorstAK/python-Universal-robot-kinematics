# Simple plotting tool by Michael Horstkoetter for use on GitHub mc-capolei/python-Universal-robot-kinematics

import numpy as np
from universal_robot_kinematics import HTrans as fwKn
from universal_robot_kinematics import invKine as inKn
from kinematicsPlot import plotArm
from numpy.linalg import inv

"""######### FORWARD KINEMATICS #########"""
# Using the current Joint angles find the position and orienation of the end
# effector

### INPUTS ###
# Robot base location (only current working location is [0, 0, 0])
Base = np.matrix([0, 0, 0])

# theta6 is not well-defined when sin(theta5) = 0 or when T16(1,3), T16(2,3) = 0
# (Because MATH)
theta1 = np.radians(45.0)
theta2 = np.radians(-135.0)
theta3 = np.radians(90.0)
theta4 = np.radians(45.0)
theta5 = np.radians(90.0)
theta6 = np.radians(1.0)

### CALLING FORWARD KINEMATIC EQUATION ###
th = np.matrix([[theta1], [theta2], [theta3], [theta4], [theta5], [theta6]])
c = [0]
T01, T02, T03, T04, T05, T06 = fwKn(th,c )

### PLOTTING ARM LOCATIONS ###
Base = np.squeeze(np.asarray(Base))
T1 = np.squeeze(np.asarray(T01))
T2 = np.squeeze(np.asarray(T02))
T3 = np.squeeze(np.asarray(T03))
T4 = np.squeeze(np.asarray(T04))
T5 = np.squeeze(np.asarray(T05))
T6 = np.squeeze(np.asarray(T06))

# An improvement would be for plotArm to take in np.matrix forms instead of
# ndarrays.
plotArm(Base, T1, T2, T3, T4, T5, T6)

"""######### INVERSE KINEMATICS #########"""
# Knowing the position and orienation of the end effector find what joint angle
# combinations are possible

### INPUTS ###
# the input will be something like the T06 shown below, but we are just going to
# use the T06 already calulated above.

#T06 = np.matrix([[ 0.0,              8.66025404e-01,  -5.00000000e-01,     3.63537488e-01],
#                 [-1.00000000e+00,   0.0,              0.0,               -1.09150000e-01],
#                 [ 0.0,              5.00000000e-01,   8.66025404e-01,     4.25598256e-01],
#                 [ 0.0,              0.0,              0.0,                1.0]], dtype=float)

desired_pos = T06
th = inKn(desired_pos)

# Columns are possible joint combinations, Rows are Joint Angles 1-6.
print(th)
