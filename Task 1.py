#-- TASK 1 --#

# Install in Console: pip install mysql-connector-python
# Install in Console: conda install matplotlib

# Import Matplotlib to Plot the Graph
import matplotlib.pyplot as plt
# Import Numpy for Array Speed
import numpy as np
# X axis parameter:
xaxis = np.array([0, 10])
# Y axis parameter:
yaxis = np.array([0, 10])
# Plot the xaxis and yaxis arrays into a Graph
plt.plot(xaxis, yaxis)
# Display the Graph
plt.show()