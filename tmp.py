import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import numpy as np
import quandl as qdmath
import loan as ln

graph = ln.loan.calc_annuity_graph(30000, 10, 12,100)

row,col = graph.shape
for r in range(row):
    print(graph[r].tolist())

df = pd.DataFrame(graph)
df.to_csv('graphs\\graph.csv',header=['PMT','Intrest','Principal','Additional_Payment','Principal Left'])
df[0:][4].plot()
plt.show()


# hpi_csv = pd.read_csv('hpi.csv')
# print(hpi_csv)

