import pandas as pd
import numpy as np


def items_info(state):
    dfs = []
    for y in ys:
        df = pd.read_csv(f'analysis/EtsySoldOrderItems{y}.csv')
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
    
    active_items = pd.read_csv('analysis/EtsyListingsDownload.csv')
    active_items['Item Name'] = active_items['TITLE']
    del active_items['TITLE']

    if state == 'Все':
        res_df = pd.merge(active_items, all_items, on='Item Name', how='inner')
        res_df = res_df.groupby('Item Name')
        res_df = res_df[['Item Name', '']]