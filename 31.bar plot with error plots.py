'''import matplotlib.pyplot as plt
import numpy as np

groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
errors_men = [2, 3, 4, 1, 2]
errors_women = [3, 5, 2, 3, 3]

bar_width = 0.5

index = np.arange(len(groups))

bars1 = plt.bar(index, means_men, bar_width, yerr=errors_men, label='Men', color='blue', capsize=5)

bars2 = plt.bar(index, means_women, bar_width, yerr=errors_women, bottom=means_men, label='Women', color='pink', capsize=5)

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.legend()

plt.show()'''


import numpy as np
import matplotlib.pyplot as plt
groups=["Group1","Group2","Group3","Group4"]
men=[12,23,34,45]
women=[23,34,45,56]
err_men=[4,3,4,1]
err_women=[3,5,2,3]
bar_width=0.35
index=np.arange(len(groups))
plt.bar(index,men,bar_width,yerr=err_men,capsize=5)
plt.bar(index,women,bar_width,yerr=err_women,bottom=men,capsize=5)
plt.show()































