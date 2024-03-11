import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------------------
# Task 1
# -----------------------------------------------------------------------------------------
data = pd.read_csv("./planets.csv")
planets = data.to_dict(orient="records")

# Task 1.1 Draw a bar chart showing the density of the planets
f1 = plt.figure(1)
planet_names = [planet["Name"] for planet in planets]
planet_densities = [planet["Density"] for planet in planets]
plt.bar(planet_names, planet_densities)
plt.title("Planets Vs. Corresponding Density")
plt.xlabel("Planets")
plt.ylabel("Density")

# Task 1.2 Draw a pie chart showing the percentage of planets with negative rotation values vs. positive rotation values
f2 = plt.figure(2)
rotation_values = [planet["Rotation"] for planet in planets]
negative_rotations = len([rotation for rotation in rotation_values if rotation < 0])
positive_rotations = len([rotation for rotation in rotation_values if rotation >= 0])

labels = ["Negative Rotations", "Positive Rotations"]
sizes = [negative_rotations, positive_rotations]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["firebrick", "forestgreen"])
plt.title("Percentage of Planets with Negative Rotations vs. Positive Rotations")
plt.axis("equal")

# Task 1.3 Draw a (multiple) line chart with x-axis as planets and y-axis as the gravity
f3 = plt.figure(3)
planets_gravity = [planet["Grav"] for planet in planets]
plt.plot(planet_names, planets_gravity, marker="o", linestyle="-", color="royalblue")
plt.title("Planets Vs. Corresponding Gravity")
plt.xlabel("Planets")
plt.ylabel("Planet Gravity")

# Task 1.4 Plot a chart of your choice using any data given in the data file
f4 = plt.figure(4)
planet_masses = [planet["Mass"] for planet in planets]
plt.scatter(planet_masses, planets_gravity, color="darkorange", marker="*")
plt.title("Planet Mass vs. Planet Gravity")
plt.xlabel("Planet Mass")
plt.ylabel("Planet Gravity")

# -----------------------------------------------------------------------------------------
# Task 2
# -----------------------------------------------------------------------------------------
data = pd.read_csv("./5000_points.txt", delimiter="\s+")
points = np.array(data)

# Task 2.1 Draw a scatter graph to show all points
f5 = plt.figure(5)
plt.scatter(points[:, 0], points[:, 1], color="darkorange")
plt.title("Scatter Plot of 5000 Points")
plt.xlabel("X")
plt.ylabel("Y")

# Task 2.2 Draw a scatter graph that shows points in even position (assume starting from index 0, i.e. P0, P2, ) with red color and points in odd position (i.e. P1, P3, …) with green color
f6 = plt.figure(6)
even_points = points[::2]
odd_points = points[1::2]
plt.scatter(even_points[:, 0], even_points[:, 1], color="firebrick", label="Even Points")
plt.scatter(odd_points[:, 0], odd_points[:, 1], color="forestgreen", label="Odd Points")
plt.title("Scatter Plot of Even and Odd Points from 5000 Points")
plt.xlabel("X")
plt.ylabel("Y")

# Task 2.3 Draw a bar comparing the number of points in these three groups (x < y, x == y, and x > y, where x and y are coordinates of a point.)
f7 = plt.figure(7)
x_less_y = len(points[points[:, 0] < points[:, 1]])
x_equals_y = len(points[points[:, 0] == points[:, 1]])
x_greater_y = len(points[points[:, 0] > points[:, 1]])

labels = ["X < Y", "X = Y", "X > Y"]
sizes = [x_less_y, x_equals_y, x_greater_y]
plt.bar(labels, sizes, color=["firebrick", "forestgreen", "royalblue"])
plt.title("Comparison of Number of Points in x < y, x = y, and x > y Groups")
plt.xlabel("Groups")
plt.ylabel("Number of Points")

# Task 2.4 Plot a chart of your choice using the data given in the data file
f8 = plt.figure(8)
plt.hist(points[:, 0], bins=100, color="royalblue")
plt.title("Histogram of X Coordinates")
plt.xlabel("X Coordinates")
plt.ylabel("Frequency")
plt.show()