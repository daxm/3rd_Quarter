#!/usr/bin/env python3
import random
import math
import statistics

num_of_values = 50
low_value = 300
high_value = 400
#number_of_values = 25
#starting_list = random.sample(range(low_value, high_value), number_of_values)
starting_list = [random.randint(low_value, high_value) for iter in range(num_of_values)]
#print(f"Starting List:{starting_list}")

# Sort list
starting_list.sort()
#print(f"Sorted starting_list: {starting_list}")

# Chop off the bottom 1/2 of starting_list
top_half = starting_list[math.floor(len(starting_list)/2):]
#print(f"Top Half of the list: {top_half}")

# Chop off the top 1/2 of top_half
third_quarter = top_half[:math.floor(len(top_half)/2)]
#print(f"3rd Quarter of the list: {third_quarter}")

# Compute Average Value of 3rd quarter
ave = sum(third_quarter)/len(third_quarter)
print(f"Average of 3rd Quarter: {int(ave)}")

### Another Method is to compute the STD and offset above the mean
suggested_value = sum(starting_list) / len(starting_list) + statistics.pstdev(starting_list)
print(f"1 STD above mean: {int(suggested_value)}")
