# 8. Drawing Line chart and Bar chart using Matplotlib
import matplotlib.pyplot as p
subjects = ['Math', 'Sci', 'Eng', 'Kan']
marks = [85, 90, 78, 88]

# Line Chart
p.plot(subjects, marks)
p.title('Student Marks - Line Chart')
p.xlabel('Subjects')
p.ylabel('Marks')
p.show()

# Bar Chart
p.bar(subjects, marks)
p.title('Student Marks - Bar Chart')
p.xlabel('Subjects')
p.ylabel('Marks')
p.show()