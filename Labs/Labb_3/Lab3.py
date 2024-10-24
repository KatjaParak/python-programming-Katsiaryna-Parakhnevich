import pandas as pd
import matplotlib.pyplot as plt


def open_data():
    data = pd.read_csv("Labs/Labb_3/unlabelled_data.csv", header=None)
    return data


def add_label(k, m, data=open_data()):
    data_values = data.values
    label_list = []

    for x, y in data_values:
        if y > (k*x + m):
            l = 1
            label_list.append(l)
        else:
            l = 0
            label_list.append(l)
    return label_list


def save_data():
    data = open_data()
    data['label'] = add_label(-1, 0)
    data.to_csv("Labs/Labb_3/labelled_data.csv", index=False)
    return data


def main():
    df = save_data()
    x_arr = df.iloc[:, 0]
    y_arr = [-1*x + 0 for x in x_arr]
    df_0 = df.loc[df['label'] == 0]
    df_1 = df.loc[df['label'] == 1]
    print(f"The quantity of points classified as 0: {len(df_0)}",
          f"\nThe quantity of points classified as 1: {len(df_1)}")

    plt.scatter(df_0[0], df_0[1], label='0')
    plt.scatter(df_1[0], df_1[1], label='1')
    plt.plot(x_arr, y_arr, '-', label='y = -x')
    plt.title("Labelled data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(fontsize=8, loc='best')
    plt.show()


if __name__ == "__main__":
    main()
