import pandas as pd
import matplotlib.pyplot as plt

# function to determine if a point lies above or below a straight line


def classify_points(k, m, df_values):
    global label_list
    label_list = []

    for i, j in df_values:
        if j > (k*i + m):
            e = 1
            label_list.append(e)
        else:
            e = 0
            label_list.append(e)
    return label_list


data = pd.read_csv("Labs/unlabelled_data.csv", header=None)
df = pd.DataFrame(data)
df_values = df.values

# calls the function
classify_points(-1, 0, df_values)

# adds a column with labels to the file
# saves the file as "labelled_data.csv"
df['label'] = label_list
df.to_csv("../labelled_data.csv", index=False)

# classifies points according to their labels
classify_points(-1, 0, df_values)
df_1 = df.loc[df["label"] == 0]
df_2 = df.loc[df["label"] == 1]
print(f"The quantity of points classified as 0: {len(df_1)}")
print(f"The quantity of points classified as 1: {len(df_2)}")


# plots the classified points with the linear function

a = data.iloc[:, 0]
b = data.iloc[:, 1]
y = [-1*x + 0 for x in a]

# classified points
a1, a2 = df_1.iloc[:, 0], df_2.iloc[:, 0]
b1, b2 = df_1.iloc[:, 1], df_2.iloc[:, 1]

fig, ax = plt.subplots()
ax.scatter(a1, b1, label='0')  # plots the points with label 0
ax.scatter(a2, b2, label='1')  # plots the points with label 1
ax.plot(a, y, '-', label='y = -x')  # plots the linear function
ax.set(title="Labelled data", xlabel='x', ylabel='y')
ax.legend(fontsize=8, loc='best')
plt.show()
