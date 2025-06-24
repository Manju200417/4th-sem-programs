#9. Drawing Histogram and Pie chart using Matplotlib 
import matplotlib.pyplot as plt

# Data
data = [12, 10, 12, 14, 19, 20, 18]
sizes = [20, 30, 25, 25]
labels = ['Math', 'Sci', 'Eng', 'Kan']

# Histogram
plt.hist(data, bins=5, edgecolor='black')
plt.title('Student Marks - Histogram')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

# Pie Chart
plt.pie(sizes, labels=labels)
plt.title('Subject Distribution - Pie Chart')
plt.show()