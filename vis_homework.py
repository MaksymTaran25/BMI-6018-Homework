# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
# %% libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# %% data

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
covid_df = pd.read_csv(url, index_col=0)

# %% Instructions

"""
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
"""

# %% viz 1
df_1 = covid_df[covid_df["Province_State"] == "Utah"]  # left only counties from Utah
df_1 = df_1.iloc[
    :, list([4]) + list(range(10, 1153))
]  # removed all columns except the one with dates and names of counties.
df_1 = df_1.set_index("Admin2")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format
df_1 = df_1.transpose()  # changed rows and columns with each other


plt.title("Dates/Cases of each County in Utah", fontsize=20)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Cases", fontsize=15)
plt.plot(
    df_1.index, df_1.values, color="gray"
)  # plotted and setted color of all lines to gray

plt.tick_params(
    axis="x", labelrotation=45
)  # rotated x-axis label so they won't overlap

plt.gca().get_lines()[20].set_color("red")  # Set Salt Lake line to red
plt.gca().get_lines()[20].set_marker("o")  # Set marked for Salt Lake
plt.gca().get_lines()[20].set_markevery(365)  # Setted it to mark every year

"""
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
"""

# %% viz 2
# I am kinda confused what was meant by the most cases to date, so I assumed that it means that I need to find two counties with most cases among other from their state and compare their cases over time.
df_1 = covid_df[covid_df["Province_State"] == "Utah"]  # left only counties from Utah
df_1 = df_1.iloc[
    :, list([4]) + list(range(10, 1153))
]  # removed all columns except the one with dates and names of counties.
df_1 = df_1.set_index("Admin2")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format

df_1["Most Cases to date"] = df_1[df_1.columns].max(
    axis=1
)  # creating column which has most cases for each county
Most_Cases_To_Date_Utah = df_1.loc[
    df_1["Most Cases to date"].idxmax()
]  # Finding row with the most cases to date among all couties in Utah.
Most_Cases_To_Date_Utah = Most_Cases_To_Date_Utah.drop(
    ["Most Cases to date"]
)  # drop column because it were not represanting date and we do not need  it anymore.
Most_Cases_To_Date_Utah.index = pd.to_datetime(
    Most_Cases_To_Date_Utah.index, format="%m/%d/%y"
)  # change date format of indices

df_1 = covid_df[
    covid_df["Province_State"] == "Florida"
]  # left only counties from Florida
df_1 = df_1.iloc[
    :, list([4]) + list(range(10, 1153))
]  # removed all columns except the one with dates and names of counties.
df_1 = df_1.set_index("Admin2")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format

df_1["Most Cases to date"] = df_1[df_1.columns].max(
    axis=1
)  # creating column which has most cases for each county
Most_Cases_To_Date_Florida = df_1.loc[
    df_1["Most Cases to date"].idxmax()
]  # Finding row with the most cases to date among all couties in Florida.
Most_Cases_To_Date_Florida = Most_Cases_To_Date_Florida.drop(
    ["Most Cases to date"]
)  # drop column because it were not represanting date and we do not need  it anymore.
Most_Cases_To_Date_Florida.index = pd.to_datetime(
    Most_Cases_To_Date_Florida.index, format="%m/%d/%y"
)  # change date format of indices

plt.title("Comparison of counties from Utah/Florida with the most cases", fontsize=15)
plt.xlabel("Date", fontsize=13)
plt.ylabel("Cases", fontsize=13)
plt.tick_params(
    axis="x", labelrotation=45
)  # rotated x-axis label so they won't overlap

plt.plot(
    Most_Cases_To_Date_Utah.index, Most_Cases_To_Date_Utah.values, label="Sale Lake"
)
plt.plot(
    Most_Cases_To_Date_Florida.index,
    Most_Cases_To_Date_Florida.values,
    label="Miami-Dade",
)
plt.ticklabel_format(
    style="plain", axis="y"
)  # remove scientific notation which was caused by big number of cases
plt.gca().get_lines()[0].set_color("red")  # Set Salt Lake line to red
plt.gca().get_lines()[0].set_marker("o")  # Set marked for Salt Lake
plt.gca().get_lines()[0].set_markevery(365)  # Setted it to mark every year
plt.gca().get_lines()[1].set_color("blue")  # Set Salt Lake line to red
plt.gca().get_lines()[1].set_marker("o")  # Set marked for Salt Lake
plt.gca().get_lines()[1].set_markevery(365)  # Setted it to mark every year

plt.legend()


"""
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
"""

# %% viz 3
df_1 = covid_df[
    covid_df["Province_State"] == "Florida"
]  # left only counties from Florida
df_1 = df_1.iloc[
    :, list([4]) + list(range(10, 1153))
]  # removed all columns except the one with dates and names of counties.
df_1 = df_1.set_index("Admin2")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format
Walton_data = df_1[df_1.index == "Walton"]  # Selecting certain county
Walton_data = Walton_data.transpose()
Walton_daily_data = Walton_data.copy()  # making copy to change it later

for n in reversed(
    range(1, 1143)
):  # range of all dates except the first one because it already contain new daily cases
    Walton_daily_data.iloc[n] = (
        Walton_daily_data.iloc[n] - Walton_daily_data.iloc[n - 1]
    )

plt.title("Running total/Daily new cases in Walton", fontsize=20)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Running total cases", fontsize=15, color="blue")

plt.tick_params(axis="y", labelcolor="blue")
plt.tick_params(
    axis="x", labelrotation=45
)  # rotated x-axis label so they won't overlap
plt.plot(Walton_data.index, Walton_data.values, label="Running total of cases")
plt.gca().twinx()  # creating new axis
plt.tick_params(axis="y", labelcolor="red")  # customizing new axis
plt.ylabel("Daily new cases", fontsize=15, color="red")
plt.plot(
    Walton_daily_data.index, Walton_daily_data.values, color="red", alpha=0.4
)  # plotting daily new cases / I made it semi-transparent by adding alpha so it wont overlap blue line
"""
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
"""

# %% viz 4
df_1 = covid_df.iloc[
    :, list(range(4, 6)) + list(range(10, 1153))
]  # removed all columns except the one with dates, state and names of counties.

mask = (
    df_1["Province_State"] == "Utah"
)  # create mask to later delete each state exept Utah

df_1 = df_1[mask]  # applying mask

df_1 = df_1.drop(columns=["Province_State"])
df_1 = df_1.set_index("Admin2")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format

df_1["Most Cases to date"] = df_1[df_1.columns].max(
    axis=1
)  # creating column which has most cases for each county
df_1 = df_1.iloc[
    :, list([1143])
]  # leaving only column with most cases to sum them later

df_1.groupby([df_1.index, df_1.sum(axis=1)]).size().unstack().plot(
    kind="bar", stacked=True
)

"""
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
"""

# %% extra credit (5 points)
df_1 = covid_df.iloc[
    :, list([5]) + list(range(10, 1153))
]  # removed all columns except the one with dates and names of counties.
df_1 = df_1.set_index("Province_State")  # Changed index to county name.
df_1.columns = pd.to_datetime(df_1.columns, format="%m/%d/%y")  #  changed date format

df_1["Most Cases to date"] = df_1[df_1.columns].max(
    axis=1
)  # creating column which has most cases for each county
df_1 = df_1.iloc[
    :, list([1143])
]  # leaving only column with most cases to sum them later

# I am not sure if I correctly understood assignment. So below I commented code which sums all counties cases and new dataframe will contain state and its total sum of cases.
# df_1 = pd.pivot_table(
#     df_1, index=["Province_State"], values=["Most Cases to date"], aggfunc="sum"
# )  # summes all cases by state

df_1 = df_1.sort_values(
    "Most Cases to date", ascending=False
)  # sort values from most to least
sns.set_theme(rc={"figure.figsize": (11.7, 10)})  # changes size

sns.boxplot(x="Province_State", y="Most Cases to date", data=df_1)
plt.ticklabel_format(
    style="plain", axis="y"
)  # remove scientific notation which was caused by big number of cases

plt.tick_params(
    axis="x", labelrotation=90
)  # rotated x-axis label so they won't overlap

plt.xlabel("State", fontsize=20)
plt.ylabel("Most Cases", fontsize=20)

"""
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
"""

# %%
