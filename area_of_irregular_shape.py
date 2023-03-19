
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

x_point = []
y_point = []

co_ords = [(5, 5), (16, 85), (40, 70), (50, 50), (30, 20)]
mapping = Polygon(co_ords)

for i in co_ords:
    a = i[0]
    b = i[1]
    x_point.append(a)
    y_point.append(b)
x_point.append(x_point[0])
y_point.append(y_point[0])
plt.plot(x_point, y_point, color="red")

n = 0
m = 0
for i in range(500):
    x = np.random.randint(0, 50)
    y = np.random.randint(0, 100)
    point = Point(x, y)
    if mapping.contains(point):
        m += 1
    n += 1
    plt.scatter(x, y)


plt.show()
predicted_area = (m/n)*(100 * 50)
print("Actual Area : ", mapping.area)
print(f"Predicted Area: {predicted_area}")
