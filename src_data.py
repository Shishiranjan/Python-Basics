import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urlib
import numpy as np

def graph_data(stock):
    print('Currently pulling:', stock)
    url = 'http://chartapi.finance.yahoo.com/instruction/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    print(url)
    
stock = input('Stock to plot:')
graph_data(stock)
