# Simple plotter by Michael Horstkoetter for use on GitHub mc-capolei/python-Universal-robot-kinematics

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def plot_vectors(vectors):
	X, Y, Z, U, V, W = zip(*vectors)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.quiver(X, Y, Z, U, V, W, pivot='tail')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_xlim([-1.1,1.1])
	ax.set_ylim([-1.1,1.1])
	ax.set_zlim([-1.1,1.1])
	plt.draw()
	plt.show()

# only used for the pupose of plotting the arms between the joint tansform positions.
def point_dis(a, b):
	d = np.sqrt(np.square(a-b))
	if a[0] > b[0]:
		d[0] = -d[0]
		if a[1] > b[1]:
			d[1] = -d[1]
			if a[2] > b[2]:
				d[2] = -d[2]
		elif a[2] > b[2]:
			d[2] = -d[2]
	elif a[1] > b[1]:
		d[1] = -d[1]
		if a[2] > b[2]:
			d[2] = -d[2]
	elif a[2] > b[2]:
		d[2] = -d[2]
	return d

def plotArm(Base, T01, T02, T03, T04, T05, T06):
	#N = np.array([nx, ny, nz])
	N01 = T01[:3, 0]
	N02 = T02[:3, 0]
	N03 = T03[:3, 0]
	N04 = T04[:3, 0]
	N05 = T05[:3, 0]
	N06 = T06[:3, 0]

	#O = np.array([ox, oy, oz])
	O01 = T01[:3, 1]
	O02 = T02[:3, 1]
	O03 = T03[:3, 1]
	O04 = T04[:3, 1]
	O05 = T05[:3, 1]
	O06 = T06[:3, 1]

	#A = np.array([ax, ay, az])
	A01 = T01[:3, 2]
	A02 = T02[:3, 2]
	A03 = T03[:3, 2]
	A04 = T04[:3, 2]
	A05 = T05[:3, 2]
	A06 = T06[:3, 2]

	#P = np.array([px, py, pz])
	P01 = T01[:3, 3]
	P02 = T02[:3, 3]
	P03 = T03[:3, 3]
	P04 = T04[:3, 3]
	P05 = T05[:3, 3]
	P06 = T06[:3, 3]

	# Joining two vectors into an array for plotting
	vecP01 = np.concatenate((Base, P01), axis=0)
	vecN01 = np.concatenate((P01, np.multiply(N01, 0.03)), axis=0)
	vecO01 = np.concatenate((P01, np.multiply(O01, 0.03)), axis=0)
	vecA01 = np.concatenate((P01, np.multiply(A01, 0.03)), axis=0)

	vecP02 = np.concatenate((P01, point_dis(P01, P02)), axis=0)
	vecN02 = np.concatenate((P02, np.multiply(N02, 0.03)), axis=0)
	vecO02 = np.concatenate((P02, np.multiply(O02, 0.03)), axis=0)
	vecA02 = np.concatenate((P02, np.multiply(A02, 0.03)), axis=0)

	vecP03 = np.concatenate((P02, point_dis(P02, P03)), axis=0)
	vecN03 = np.concatenate((P03, np.multiply(N03, 0.03)), axis=0)
	vecO03 = np.concatenate((P03, np.multiply(O03, 0.03)), axis=0)
	vecA03 = np.concatenate((P03, np.multiply(A03, 0.03)), axis=0)

	vecP04 = np.concatenate((P03, point_dis(P03, P04)), axis=0)
	vecN04 = np.concatenate((P04, np.multiply(N04, 0.03)), axis=0)
	vecO04 = np.concatenate((P04, np.multiply(O04, 0.03)), axis=0)
	vecA04 = np.concatenate((P04, np.multiply(A04, 0.03)), axis=0)

	vecP05 = np.concatenate((P04, point_dis(P04, P05)), axis=0)
	vecN05 = np.concatenate((P05, np.multiply(N05, 0.03)), axis=0)
	vecO05 = np.concatenate((P05, np.multiply(O05, 0.03)), axis=0)
	vecA05 = np.concatenate((P05, np.multiply(A05, 0.03)), axis=0)

	vecP06 = np.concatenate((P05, point_dis(P05, P06)), axis=0)
	vecN06 = np.concatenate((P06, np.multiply(N06, 0.03)), axis=0)
	vecO06 = np.concatenate((P06, np.multiply(O06, 0.03)), axis=0)
	vecA06 = np.concatenate((P06, np.multiply(A06, 0.03)), axis=0)

	vectors = np.array([vecP01, vecN01, vecO01, vecA01,
					vecP02, vecN02, vecO02, vecA02,
					vecP03, vecN03, vecO03, vecA03,
					vecP04, vecN04, vecO04, vecA04,
					vecP05, vecN05, vecO05, vecA05,
					vecP06, vecN06, vecO06, vecA06])

	plot_vectors(vectors)
