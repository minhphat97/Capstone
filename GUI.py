
from matplotlib import image
from matplotlib import pyplot as plt
  
# to read the image stored in the working directory
data = image.imread('net2.jpg')
  
# to draw a line from (200,300) to (500,100)
x = [268, 507]
y = [1408, 792]
plt.plot(x, color="black", linewidth=3)
plt.imshow(data)
plt.show()