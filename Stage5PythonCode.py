import statistics
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.rc('xtick', labelsize=5) 
plt.rc('ytick', labelsize=5) 

# plot avg number of clicks over optimal by participants
plt.subplot(4, 2, 1)
xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([1, .2174, .5625, .4783, .5621])

mean = statistics.mean(ypoints)
stddev = statistics.stdev(ypoints)

plt.xlabel("Participant", fontsize=5)
plt.ylabel("Clicks", fontsize=5)
plt.title("Average Clicks Over Optimal/Task \n Mean: " + str(mean) + "\n   Std Dev: " + str(stddev), fontsize=5)

plt.plot(xpoints, ypoints, marker="o")
plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))

# plot total errors by participants
plt.subplot(4, 2, 2)
xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([23, 5, 13, 11, 13])

mean = statistics.mean(ypoints)
stddev = statistics.stdev(ypoints)

plt.plot(xpoints, ypoints, marker="o")
plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))
plt.yticks(np.arange(min(ypoints), max(ypoints)+1, 5.0))

plt.xlabel("Participant", fontsize=5)
plt.ylabel("Errors", fontsize=5)
plt.title("Total Errors Over All Tasks \n Mean: " + str(mean) + "\n   Std Dev: " + str(stddev), fontsize=5)

# plot avg time per by participants
plt.subplot(4, 2, 3)
xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([24, 14, 19, 23, 26])

mean = statistics.mean(ypoints)
stddev = statistics.stdev(ypoints)

plt.xlabel("Participant", fontsize=5)
plt.ylabel("Seconds", fontsize=5)
plt.title("Average Time Per Task (sec) \n Mean: " + str(mean) + "\n   Std Dev: " + str(stddev), fontsize=5)

plt.plot(xpoints, ypoints, marker="o")
plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))
plt.yticks(np.arange(min(ypoints), max(ypoints)+1, 5.0))

# plot number of long pauses by participants
plt.subplot(4, 2, 4)
xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([6, 2, 1, 2, 2])

mean = statistics.mean(ypoints)
stddev = statistics.stdev(ypoints)

plt.xlabel("Participant", fontsize=5)
plt.ylabel("Pauses", fontsize=5)
plt.title("Number of Pauses Longer than 2-3 Seconds \n Mean: " + str(mean) + "\n   Std Dev: " + str(stddev), fontsize=5)

plt.plot(xpoints, ypoints, marker="o")
plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))
plt.yticks(np.arange(min(ypoints), max(ypoints)+1, 1.0))

# plot improvement in repeated tasks by participants
plt.subplot(4, 2, 5)
xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([-32, -11, 2, -10, -9])

mean = statistics.mean(ypoints)
stddev = statistics.stdev(ypoints)

plt.xlabel("Participant", fontsize=5)
plt.ylabel("Seconds", fontsize=5)
plt.title("Improvement In  Completing Repeated Tasks (sec) \n Mean: " + str(mean) + "\n   Std Dev: " + str(stddev), fontsize=5)

plt.plot(xpoints, ypoints, marker="o")
plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))
plt.yticks(np.arange(min(ypoints), max(ypoints)+1, 5.0))

plt.tight_layout(h_pad=1)

# pie chart on tasks given up by participants
labels = ["Yes", "No"]
sizes = [1, 4]
plt.subplot(4, 2, 6).pie(sizes, labels=labels, autopct='%.0f%%', textprops={'size': 'smaller'}, radius=1.9)
plt.title("Failed A Task", fontsize = 5, bbox={'facecolor':'0.8', 'pad':5})

# pie chart on 3 tasks completed correctly in a row by participants
labels = ["Yes", "No"]
sizes = [1, 4]
plt.subplot(4, 2, 7).pie(sizes, labels=labels, autopct='%.0f%%', textprops={'size': 'smaller'}, radius=1.9)
plt.title("3 Successful Tasks In A Row", fontsize = 5, loc='right', bbox={'facecolor':'0.8', 'pad':5})

plt.show()