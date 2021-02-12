import matplotlib.pyplot as plt

test_score = [41, 67, 74, 49, 82, 88, 86, 91, 73, 48, 53, 57, 93, 71, 42, 59, 49, 69, 79, 89]

x = [x for x in range(len(test_score))]

plt.bar(x, test_score)

plt.show()

bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(test_score, bins,  histtype='bar', rwidth=0.4)

plt.show()
