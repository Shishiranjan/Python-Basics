import matplotlib.pyplot as plt

test_score = [41, 67, 74, 49, 82, 88.5, 86.5, 91, 73.5, 48, 53, 57, 93, 71, 42, 59, 49, 69, 79, 89]
time_spent = [14, 23, 27, 41, 35, 54, 29, 39.5, 19, 49.5, 41, 52.5, 47, 33, 22, 44, 55, 11, 46, 57]

plt.scatter(test_score, time_spent, marker = 'o', color = 'y', cmap = 'image.cmap' )

plt.title('Correlation between score of test and time spent on test in minutes')
plt.xlabel('Time spent on test')
plt.ylabel('Test score')
plt.show()

#Scatter plot is basically used to derive a correlation between groups. As for example shown above It describes the relationship between the score of the test and the
# time spent on test in minutes having the threshold value of 60 minutes. 
