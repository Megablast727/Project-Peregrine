import numpy as np
import matplotlib.pyplot as plt
from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.plotting import StaticOrbitPlotter

# Define initial conditions
r = [7000, 0, 0]  # Position vector in km
v = [0, 7.5, 0]   # Velocity vector in km/s

# Create an orbit object
orbit = Orbit.from_vectors(Earth, r, v)

# Plot the orbit
fig, ax = plt.subplots()
plotter = StaticOrbitPlotter(ax)
plotter.plot(orbit, label="Spacecraft Orbit")

plt.show()
