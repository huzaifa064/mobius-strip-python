import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------
# Möbius Strip
# f(u,v) =
# ((R + u*sin(v/2))*cos(v),
#  (R + u*sin(v/2))*sin(v),
#  u*cos(v/2))
# ---------------------------------------

# INPUT
R = float(input("Enter R (radius): "))
a = float(input("Enter a (half-width): "))
resolution = int(input("Enter resolution (e.g. 100): "))


# Parameter ranges
u = np.linspace(-a, a, resolution)
v = np.linspace(0, 2 * np.pi, resolution)


# Create a grid of u and v values
U, V = np.meshgrid(u, v)


# Möbius strip equation
X = (R + U * np.sin(V / 2)) * np.cos(V)
Y = (R + U * np.sin(V / 2)) * np.sin(V)
Z = U * np.cos(V / 2)


# Create 3D figure
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")


# Draw surface
ax.plot_surface(
    X, Y, Z,
    cmap="viridis",
    edgecolor="none"
)


# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("Möbius Strip")


# Make proportions equal
ax.set_box_aspect([1, 1, 0.5])


plt.show()