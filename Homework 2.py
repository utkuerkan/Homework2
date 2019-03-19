# Getting number of points
n = int(input ("Please define n="))

# Getting coordinates from user
coordinates = []
for i in range(1, n):
    raw= input("Please enter " + str(i) + "th coordinates ").split( "," )
    x = float(raw[0])
    y = float(raw[1])
    point=(x,y)
    coordinates.append( point )
print("Coordinates:", coordinates)

# Calculating center of mass
sumx = 0
sumy = 0
for point in coordinates:
    sumx += point[0]
    sumy += point[1]
center_of_mass = (sumx/n, sumy/n)
print("Center of mass:", center_of_mass)

# Calculate distances
distances = []
for point, idx in zip(coordinates, range(n)):
    distance = (center_of_mass[0]-point[0])**2 + (center_of_mass[1]-point[1])**2
    distance = distance**.5
    distances.append( (distance, idx) )
print("Distances are:", distances)

# Find closest point
closest_point = distances[0]
for distance, idx in distances:
    if distance < closest_point[0]:
        closest_point = (distance, idx)
print("Closest point is:", coordinates[closest_point[1]], "with distance:", closest_point[0])

# Find furthest point
furthest_point = distances[0]
for distance, idx in distances:
    if distance >furthest_point[0]:
        furthest_point = (distance, idx)
print("Furthest point is:", coordinates[furthest_point[1]], "with distance:", furthest_point[0])