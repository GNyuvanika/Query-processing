import matplotlib.pyplot as plt
import numpy as np

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

bar_width = 0.35

index = np.arange(len(groups))

bars1 = plt.bar(index, means_men, bar_width, label='Men', color='blue')
bars2 = plt.bar(index + bar_width, means_women, bar_width, label='Women', color='pink')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.legend()
plt.show()
