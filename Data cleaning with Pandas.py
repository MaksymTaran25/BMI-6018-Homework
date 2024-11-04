# Importing required libraries.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing my data.
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)

flights_data.drop(columns=flights_data.columns[0], axis=1, inplace=True) # For some reason after importing data, there was a new "Unnamed: 0" column, which from my point of view is irrelevant because it were just indexes. So I removed it.
flights_data.index = flights_data.index + 1 # To start indexing from 1 instead of 0 (I just find even more convenient)

weather_data_pd = pd.read_csv('weather.csv')

weather_data_pd.drop(columns=weather_data_pd.columns[0], axis=1, inplace=True) # For some reason after importing data, there was a new "Unnamed: 0" column, which from my point of view is irrelevant because it were just indexes. So I removed it.
weather_data_pd.index = weather_data_pd.index + 1 # To start indexing from 1 instead of 0 (I just find even more convenient)

weather_data_np = weather_data_pd.to_numpy()

# Question 1
Flights_from_JFK_to_SLC = flights_data[(flights_data["origin"] == "JFK") & (flights_data["dest"] == "SLC")] # Creates another DataFrame where column "origin" contains only values "JFK" and column "dest" contains only values "SLC".

q_1 = Flights_from_JFK_to_SLC.shape[0] # assigning result to answer variable as it was specified in the assignment
print("1) Amount of flights from JFK to SLC is:", q_1) # Returns amount of rows of "Amount_of_flights", to put it more simple this is amount of fligths from JFK to SLC.

# Question 2 - I couldn't understand whether I should calculate total amount of flights provided by certain airlines or just amount of unique airlines, so I decided to calculate amount of Airlines.
Flights_to_SLC = flights_data[flights_data["dest"] == "SLC"] # Creates another DataFrame where column "dest" contains only values "SLC".

q_2 = Flights_to_SLC["carrier"].nunique() # assigning result to answer variable as it was specified in the assignment
print("2) Amount of airlines which fly to SLC is:", q_2) # I found that I can use "nunique()"" to get a number of unique values from column. If I understand correctly, column "carrier" contains name of airlines, so I just counted number of unique airlines after I filtered it.

# Question 3
Flights_to_RDU = flights_data[flights_data["dest"] == "RDU"] # Creates another DataFrame where column "dest" contains only values "RDU".

q_3 = Flights_to_RDU["arr_delay"].mean() # assigning result to answer variable as it was specified in the assignment
print("3) Average arrival delay for flights to RDU is:", q_3) # I used "mean()" to calculate average of all values in the "arr_delay" column of my filtered DataFrame.

# Question 4
Flights_to_SEA = flights_data[flights_data["dest"] == "SEA"] # Creates another DataFrame where column "dest" contains only values "SLC".
Flights_from_LGA_JFK_to_SEA = flights_data[(flights_data["dest"] == "SEA") & ((flights_data["origin"] == "JFK") | (flights_data["origin"] == "LGA"))] # Creates another DataFrame where column "origin" contains only values "JFK" or "LGA" and column "dest" contains only values "SEA".

q_4 = Flights_from_LGA_JFK_to_SEA.shape[0] / Flights_to_SEA.shape[0] # assigning result to answer variable as it was specified in the assignment
print("4) Proportion of flights to SEA from JFK and LGA to total amount of flights to SEA is:", q_4) # Caclulates proportion of flights to SEA from JFK and LGA to totall amount of flights to SEA.

# Question 5
Date_of_flights_data = flights_data.copy() # Created copy of original dataframe to make my changes.
Date_of_flights_data["date"] = Date_of_flights_data["year"].astype(str) + "/" + Date_of_flights_data["month"].astype(str) + "/" + Date_of_flights_data["day"].astype(str) # Created new column "date" which combines "year", "month", "day" by given format.

Date_of_flights_dep_data = Date_of_flights_data[["date", "dep_delay"]] # To put it more simple, created new dataframe with dropped columns , so that only "date" and "dep_delay" remains.
Date_of_flights_dep_data = Date_of_flights_dep_data.groupby(["date"]).mean() # Groups by "date" columns and returns mean value of "dep_delay" for each value of "date".
Date_of_flights_dep_data = Date_of_flights_dep_data.sort_values("dep_delay", ascending=False) # Sorts in the way that the first value is the one with the largest departure delay time.

q_5 = Date_of_flights_dep_data # assigning result to answer variable as it was specified in the assignment
print(q_5) # Prints slice with mean departure values grouped by dates.

# Question 6
Date_of_flights_arr_data = Date_of_flights_data[["date", "arr_delay"]] # # To put it more simple, created new dataframe with dropped columns , so that only "date" and "arr_delay" remains (I used dataframe with dates from the previous question).
Date_of_flights_arr_data = Date_of_flights_arr_data.groupby(["date"]).mean() # Groups by "date" columns and returns mean value of "arr_delay" for each value of "date".
Date_of_flights_arr_data = Date_of_flights_arr_data.sort_values("arr_delay", ascending=False) # Sorts in the way that the first value is the one with the largest arrival delay time.

q_6 = Date_of_flights_arr_data # assigning result to answer variable as it was specified in the assignment
print(q_6)

# Question 7 
Flights_from_LGA_JFK = flights_data.copy() # copy of original DataFrame
Flights_from_LGA_JFK["speed"] = Flights_from_LGA_JFK["distance"] / Flights_from_LGA_JFK["air_time"] # adding speed column
q_7 = Flights_from_LGA_JFK.loc[(flights_data["origin"] == "JFK") | (flights_data["origin"] == "LGA") & (flights_data["year"] == 2013) ,["tailnum", "speed"]] # creating a slice

print(q_7.sort_values("speed", ascending=False)) #printing sorted slice

# Question 8
weather_data_pd = weather_data_pd.fillna(0) # replaced all nan values with 0s.
print(weather_data_pd)

# Question 9
q_9 = np.count_nonzero(weather_data_np[:,2] == 2) # counts instances of 2 at the 3rd column which in our case contains months. To put it more simple, we count amount of observation at February.
print("9) Observations made in Feburary:", q_9)

# Question 10 - It was not specified how I should find the values, so I decided to firstly create array with values recorded in february, which means month = 2. Then only leave humidity in this array and perform all actions on array with 1 column.
filtered_weather_data_np = np.delete(weather_data_np, np.where((weather_data_np[:,2] != 2))[0], axis=0) # Created array with observations only at february
filtered_weather_data_np = filtered_weather_data_np[:,7] # get only columns with humidity values for further calculations

q_10 = filtered_weather_data_np.mean() #finding mean for the whole array, in my case it is just the humidity values.

print("10) The mean humidity in February was:", q_10)

# Question 11 - I am going to use same numpy array with humidity values for this question
q_11 = filtered_weather_data_np.std() #finding std for the whole array, in my case it is just the humidity values.

print("11) The std for humidity in February was:", q_11)