import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import numpy as np
import loan as ln
import datetime as date
from dateutil.relativedelta import relativedelta

now = date.datetime.today().date()

PV, DURATION, RATE, ADD_PAY = 30000, 10, 10, 0
graph = ln.loan.calc_annuity_graph(PV, DURATION, RATE, ADD_PAY)
#ln.loan.save_graph_to_csv(graph, 'graphs\\graph.csv')
#ln.loan.print_graph(graph,PV,RATE ,ADD_PAY)

def add_month_to_currdate(months_to_add):
    return now + relativedelta(months=months_to_add)

df = pd.DataFrame(graph, columns=['PMT', 'Interest', 'Principal', 'Add_Pay', 'Principal_Left'])
df['date'] = list(map(add_month_to_currdate, df.index))
df.set_index('date', inplace=True)
df.index = pd.to_datetime(df.index)
DF_A = df.resample('A').sum()
DF_Q = df.resample('Q').sum()
# print(DF_A)
print(df.head())
# print(DF_Q.head())

# print([ '%.2f' % elem for elem in df['Principal'].tolist()])
# print(pd.DataFrame.to_json(df, orient='index'))






