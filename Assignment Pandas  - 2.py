# Importing required libraries.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Assignment 1 - For this assignment I assume that index is x and value is y of my point / Since indexes will be the same for both points in the formula they will destroy each other so my formula will be more simple: q-p
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


def EuclideanDistance(
    series1, series2
):  # This method takes 2 series as an arguments and calculates Euclidean Distance between them. For the formula I assumed that points are for example : p (0, 1) and q (0, 10) or p (1, 2) and q (1, 9)
    EDseries = pd.Series([])
    for i in range(series1.count()):
        EDseries[i] = abs(series1[i] - series2[i])
    return EDseries


print(EuclideanDistance(p, q))
print("-----------------------------")  # To separate results on terminal

# Assignment 2
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list("abcde"))
df = df[["c", "b", "a", "d", "e"]]
print(df)
print("-----------------------------")  # To separate results on terminal

# Assignment 3
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list("abcde"))


def SwapColumns(
    dataframe, first, second
):  # I decided to use indexes for interchanging columns. I found out I can use "get_loc" to get index by column name.
    firstindex = dataframe.columns.get_loc(
        first
    )  # assigning index of first column to variable
    secondindex = dataframe.columns.get_loc(
        second
    )  # assigning index of second column to variable
    dataframe.insert(
        firstindex, second, dataframe.pop(second)
    )  # inserts second column at the index of the first and then removes the old one
    dataframe.insert(
        secondindex, first, dataframe.pop(first)
    )  # inserts first column at the index of the second and then removes the old one


SwapColumns(df, "a", "c")
print(df)
print("-----------------------------")  # To separate results on terminal

# Assignemnt 4
df = pd.DataFrame(np.random.random(4) ** 10, columns=["random"])

df["random"] = df["random"].map("{:,.4f}".format)
print(df)
print("-----------------------------")  # To separate results on terminal

# Assignment 5 - I am not sure but I believe there is a mistake in the provided example of this assignment.
df = pd.DataFrame(
    np.random.randint(1, 100, 40).reshape(10, -1),
    columns=list("pqrs"),
    index=list("abcdefghij"),
)


def NearestColumnByEuclidianDistance(Dataframe):
    templist1 = []  # created list to store distances
    templist2 = []  # created list to store nearest rows
    for i in range(Dataframe.shape[0]):
        nearest = ""  # created empty string to later store rows
        min = 1000  # created int 1000 to find minimum distance in the following loop
        for a in range(Dataframe.shape[0]):
            if i != a:  # if row a does not equal row i
                distance = math.dist(
                    Dataframe.iloc[i], Dataframe.iloc[a]
                )  # find Euclidian Distance between 2 different rows
                if min > distance:  # if min is more huge that distance
                    nearest = chr(97 + a)  # set the row with nearest distance
                    min = distance  # set new min
        templist1.append(min)  # append minimum distance to list
        templist2.append(nearest)  # append nearest row to list
    Dataframe["nearest_row"] = templist2  # giving column values of list
    Dataframe["dist"] = templist1


NearestColumnByEuclidianDistance(df)
print(df)

d = {
    "p": pd.Series(
        [57, 68, 74, 80, 93, 69, 39, 63, 18, 79],
        index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ),
    "q": pd.Series(
        [77, 5, 40, 17, 48, 55, 23, 28, 4, 12],
        index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ),
    "r": pd.Series(
        [13, 92, 18, 39, 85, 8, 88, 25, 73, 45],
        index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ),
    "s": pd.Series(
        [62, 24, 37, 60, 33, 11, 53, 61, 7, 34],
        index=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ),
}
dftest = pd.DataFrame(
    d
)  # I created same dataframe as in example to test my function for sure
NearestColumnByEuclidianDistance(dftest)
print(dftest)
print("-----------------------------")  # To separate results on terminal

# Assignment 6
data = {
    "A": [45, 37, 0, 42, 50],
    "B": [38, 31, 1, 26, 90],
    "C": [10, 15, -10, 17, 100],
    "D": [60, 99, 15, 23, 56],
    "E": [76, 98, -0.03, 78, 90],
}

MyDataFrame = pd.DataFrame(data)
print(MyDataFrame.corr())
