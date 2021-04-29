#from seasonal import fit_seasons, adjust_seasons
import statsmodels.api as sm
import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import os


def create_csv(ys, path):
    list_dir = os.listdir(path)
    if 'active_items_' + '_'.join([str(y) for y in ys]) + '.csv' not in list_dir:
        dfs = []
        for y in ys:
            df = pd.read_csv(path + f'/EtsySoldOrderItems{y}.csv')
            dfs.append(df)
        
        for df in dfs:
            y = int('20' + df['Sale Date'].iloc[0].split('/')[-1])  # строка с годом таблицы
            df['y'] = [y]*len(df)
            
        cur_year = date.today().year
        def change(x):
            if str(x[1]) in x[0]:
                x[0] = x[0].replace(str(int(x[1])), str(cur_year))
            if str(x[1] + 1) in x[0]:
                x[0] = x[0].replace(str(int(x[1] + 1)), str(cur_year + 1))
            if str(x[1] - 1) in x[0]:
                x[0] = x[0].replace(str(int(x[1] - 1)), str(cur_year - 1))
            return x[0]

        for df in dfs:
            df['Item Name'] = df[['Item Name', 'y']].apply(change, axis=1)

        all_items = dfs[0]  # Объединяем таблицы в одну...
        for i in range(1, len(dfs)):
            all_items = all_items.append(dfs[i])
        
        active_items = pd.read_csv(path + '/EtsyListingsDownload.csv')
        active_items['Item Name'] = active_items['TITLE']
        del active_items['TITLE']

        # Получаем историю покупока активных товаров
        active_items = pd.merge(active_items, all_items, on='Item Name', how='left')

        active_items = active_items[['Item Name', 'Sale Date', 'Quantity', 'Item Total', 'y']]
        active_items['Sale Date'] = pd.to_datetime(active_items['Sale Date'])
        active_items = active_items.sort_values(by='Sale Date')

        min_date = active_items['Sale Date'].iloc[0]
        active_items['days'] = active_items['Sale Date'] - min_date
        active_items['days'] = active_items['days'].apply(lambda x: x.days)
        active_items['dy'] = active_items['y'] - active_items['y'].min()
        active_items['month'] = active_items['Sale Date'].apply(lambda x: x.month)
        active_items['month'] = active_items['month'] + active_items['dy']*12
        active_items.to_csv(path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
    return

def seasonal_all(ys, path):
    list_dir = os.listdir(path)
    if 'all_seasons_' + '_'.join([str(y) for y in ys]) + '.txt' not in list_dir:
        create_csv(ys, path)
        active_items = pd.read_csv(path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
        # cделаем здесь общий анализ по всем активным товарам
        active_items = active_items.groupby('month')['Item Total'].sum()
        active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])  # ?????????
        active_items = active_items.iloc[:-1]
        result = sm.tsa.seasonal_decompose(active_items['Item Total'].values, model='multiplicative', period=12)

        with open(path + '/all_seasons_' + '_'.join([str(y) for y in ys]) + '.txt', 'w') as f:
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.trend]) + '\n')
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.seasonal]) + '\n')
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.resid]))
    return

def item_seasonal(ys, path, item):
    list_dir = os.listdir(path)
    if item + '_' + '_'.join([str(y) for y in ys]) + '.txt' not in list_dir:
        create_csv(ys, path)
        active_items = pd.read_csv(path + '/active_items_' + '_'.join([str(y) for y in ys]) + '.csv')
        active_items = active_items[active_items['Item Name'] == item]
        active_items = active_items.groupby('month')['Item Total'].sum()
        active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['month', 'Item Total'])  # ?????????
        active_items = active_items.iloc[:-1]
        result = sm.tsa.seasonal_decompose(active_items['Item Total'].values, model='multiplicative', period=12)
        
        with open(path + '/' + item + '_' + '_'.join([str(y) for y in ys]) + '.txt', 'w') as f:
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.trend]) + '\n')
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.seasonal]) + '\n')
            f.write(', '.join([str(s) if str(s) != 'nan' else 'None' for s in result.resid]))
    return
