import numpy as np
import pandas as pd
import requests
import math
import xlsxwriter

# Importing our List of Stocks
stocks = pd.read_csv("../sp_500_stocks.csv")
print(stocks)

# Acquiring an API Token

