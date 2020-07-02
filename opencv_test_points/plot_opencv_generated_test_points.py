"""
Plotting the random points used for binary pixel tests in BRIEF OpenCV implementation.
They should be picked from a Gaussian distribution around the centre of the patch, 
as described in the original BRIEF paper.

Points taken from:
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_16.i
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_32.i
https://github.com/opencv/opencv_contrib/blob/4.3.0/modules/xfeatures2d/src/generated_64.i

"""
import matplotlib.pyplot as plt


file1 = open('generated_16.txt', 'r') 
count = 0


x_coords = []
y_coords = []
 
while True: 
    count += 1
    line = file1.readline() 
  
    if not line: 
        break

    x_coord = int(line[1: line.find(",")])
    y_coord = int(line[line.find(",") + 1: -2])
    x_coords.append(x_coord)
    y_coords.append(y_coord)
    print(x_coord, y_coord)
file1.close() 

plt.figure(figsize=(8,8))
plt.scatter(x_coords, y_coords)
plt.show()

plt.figure(figsize=(8,8))
for i in range(0, len(x_coords), 2):
    plt.plot(x_coords[i:i+2], y_coords[i:i+2], 'ro-')

plt.show()
