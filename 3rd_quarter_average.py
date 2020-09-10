#!/usr/bin/env python3
import random
import math

# Make a list of 25 random numbers between 5 and 60.
low_value = 5
high_value = 60
number_of_values = 25
starting_list = random.sample(range(low_value, high_value), number_of_values)
print(f"Starting List:{starting_list}")

# Sort list
starting_list.sort()
print(f"Sorted starting_list: {starting_list}")

# Chop off the bottom 1/2 of starting_list
top_half = starting_list[math.floor(len(starting_list)/2):]
print(f"Top Half of the list: {top_half}")

# Chop off the top 1/2 of top_half
third_quarter = top_half[:math.floor(len(top_half)/2)]
print(f"3rd Quarter of the list: {third_quarter}")

# Compute Average Value of 3rd quarter
ave = sum(third_quarter)/len(third_quarter)
print(f"Average of 3rd Quarter: {ave}")
