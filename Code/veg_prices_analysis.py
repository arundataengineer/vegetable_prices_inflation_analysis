# importing the necessary libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

veg_prices_file = r'C:\Users\Arun Raja\OneDrive\Desktop\Python_Training\vegetable_prices_inflation_analysis\vegetable_prices_inflation_analysis\Vegetable_Purchase\vegetable_prices.csv'

# importing the data to pandas
prices_df = pd.read_csv(filepath_or_buffer = veg_prices_file)
#print(prices_df.head(5))
#print(prices_df.tail(5))

# Checking for nulls in the dataset
#print(prices_df.isnull().sum())
