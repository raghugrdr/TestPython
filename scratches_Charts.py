# import matplotlib.pyplot as plt
#
# # defining labels
# activities = ['eat', 'sleep', 'work', 'play']
#
# # portion covered by each label
# slices = [3, 7, 8, 6]
#
# # color for each label
# colors = ['r', 'y', 'g', 'b']
#
# # plotting the pie chart
# plt.pie(slices, labels = activities, colors=colors,
# 		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
# 		radius = 1.2, autopct = '%1.1f%%')
#
# # plotting legend
# plt.legend()
#
# # showing the plot
# plt.show()


# importing the required modules
# import matplotlib.pyplot as plt
# import numpy as np
#
# # setting the x - coordinates
# x = np.arange(0, 2*(np.pi), 0.1)
# # setting the corresponding y - coordinates
# y = np.sin(x)
#
# # potting the points
# plt.plot(x, y)
#
# # function to show the plot
# plt.show()



# import required package
import pygmaps

# maps method return map object
# 1st argument is center latitude
# 2nd argument is center longitude
# 3ed argument zoom level
mymap1 = pygmaps.maps(30.3164945, 78.03219179999999, 15)

# create the html file which include
# google map. Pass the absolute path
# as an argument.
mymap1.draw('pygmap1.html')
