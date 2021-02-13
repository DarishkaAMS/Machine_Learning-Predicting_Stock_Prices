import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.model import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# Load Data
company = "FB"

start = dt.datetime(2012,2,2)
end = dt.datetime(2021,1,1)

data = web.DataReader(company, 'yahoo', start, end)

