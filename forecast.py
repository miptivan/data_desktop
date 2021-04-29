import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os


def forecast(ys, path):
    list_dir = os.listdir(path)
    if 'forecast' + '_'.join([str(y) for y in ys]) + '.txt' not in list_dir:
        active_items = pd.read_csv(path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
        active_items = active_items.groupby('month')['Item Total'].sum()
        active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])  # ?????????
        active_items = active_items.iloc[:-1]
        model = sm.tsa.ExponentialSmoothing(active_items['Item Total'].values, seasonal_periods=12, trend='mul', seasonal='mul').fit()
        res = model.forecast(12)
        print(model.trend)
        plt.plot(range(len(active_items['Item Total'])), active_items['Item Total'].values)
        plt.plot(range(len(active_items['Item Total'])), model.season*(model.trend*model.level) + model.resid)
        plt.plot(range(len(active_items['Item Total']) - 1, len(active_items['Item Total']) + len(res)), np.hstack((active_items['Item Total'].values[-1], res)))
        plt.show()
    

forecast(range(2015, 2020), 'analysis')


