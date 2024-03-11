import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./data/planets.csv")

planets = data.to_dict(orient="records")

# Task 1.1 Draw a bar chart showing the density of the planets.
f1 = plt.figure(1)
planet_names = [planet["Name"] for planet in planets]
planet_densities = [planet["Density"] for planet in planets]
plt.bar(planet_names, planet_densities)

# Task 1.2 Draw a pie chart showing the percentage of planets with negative rotation values vs. positive rotation values.
f2 = plt.figure(2)
rotation_values = [planet["Rotation"] for planet in planets]
negative_rotations = len([rotation for rotation in rotation_values if rotation < 0])
positive_rotations = len([rotation for rotation in rotation_values if rotation >= 0])

labels = ["Negative Rotations", "Positive Rotations"]
sizes = [negative_rotations, positive_rotations]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["firebrick", "forestgreen"])
plt.axis("equal")

# Task 1.3 Draw a (multiple) line chart with x-axis as planets and y-axis as the gravity
f3 = plt.figure(3)
planets_gravity = [planet["Grav"] for planet in planets]
plt.plot(planet_names, planets_gravity, marker="o", linestyle="-", color="royalblue")

# Task 1.4 Plot a chart of your choice using any data given in the data file
f4 = plt.figure(4)
planet_masses = [planet["Mass"] for planet in planets]
plt.scatter(planet_masses, planets_gravity, color="gold", marker="*")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

# -----------------------------------------------------------------------------------------
import csv

with open("./data/5000_points.txt", "r") as file:
    reader = csv.reader(file, delimiter="")
    for row in reader:
        print(row)

# Task 2.1 Draw a scatter graph to show all points
f5 = plt.figure(5)
