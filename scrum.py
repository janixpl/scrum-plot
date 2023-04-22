import matplotlib.pyplot as plt
from itertools import product 

ax = plt.figure().add_subplot(projection='3d')
arr = [1,2,3,4,5]
data = list(product(arr, arr, arr))

X = []
Y = []
Z = []
S = []

for x, y, z in data:
    X.append(x)
    Y.append(y)
    Z.append(z)
    S.append((x+y+z)**3)

#print(S)

ax.scatter(X, Y, Z, s=S, label="Stories 'Size' = Time+Unknowns+Complexity")
ax.plot([0,5], [0,5], [0,5],c=[1,0,0,1])

# Make legend, set axes limits and label
ax.legend()
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)
ax.set_xlabel('Time')
ax.set_ylabel('Unknowns')
ax.set_zlabel('Complexity')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()