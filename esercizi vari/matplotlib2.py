import matplotlib.pyplot as plt

data = {'Windows7': 48, 'Windows10': 28, 'WindowsXP': 9, 'MacOS': 7, 'Other': 6, 'Linux': 2}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(100, 30), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle("Most used OS\
                                          Based on a survey of 100 users")


plt.show()
#How can I prevent operating system names from overlapping?
