import pandas as pd
import plotly.figure_factory as ff
import numpy as np

df = pd.read_csv('phone_data.csv')
print(df.avg)

hist_data = [df.avg]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
fig.show()
