import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

df = pd.read_csv(r"/home/malou/Documents/Master/Seminars/CS_Assignment-master/istherecorrelation.csv", delimiter=";",decimal=',')
print(df)

fig = plt.figure(dpi=300)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Year'], df['WO [x1000]'], df['NL Beer consumption [x1000 hectoliter]'])
ax.set_xlabel("Year")
ax.set_ylabel("WO [x1000]")
ax.set_zlabel("NL Beer consumption [x1000 hectoliter]")
plt.title("Correlation graph, dpi=300")
plt.show()
plt.savefig("Correlation")

