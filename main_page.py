import pandas as pd
import numpy as np
from datetime import date


def main_info(ys, path):
    dfs = []
    for y in ys:
        df = pd.read_csv(path + f'/EtsySoldOrderItems{y}.csv')
        dfs.append(df)
    
    for df in dfs:
        y = int('20' + df['Sale Date'].iloc[0].split('/')[-1])  # строка с годом таблицы
        df['y'] = [y]*len(df)
    
    cur_year = date.today().year - 1
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
    
    first_sale = all_items['Sale Date'].min()
    all_count = str(all_items['Quantity'].sum())
    all_sold = str(all_items['Item Total'].sum()) + ' usd'

    active_items = pd.read_csv(path + '/EtsyListingsDownload.csv')
    active_items['Item Name'] = active_items['TITLE']
    del active_items['TITLE']

    active_items = pd.merge(active_items, all_items, on='Item Name', how='left')
    active_items = active_items.groupby('Item Name')['Item Total'].sum()
    active_items = pd.DataFrame(data=np.array([active_items.index, active_items.values]).T, columns=['Item Name', 'Item Total'])
    top_ten = active_items.sort_values(by='Item Total', ascending=False).iloc[:10]
    return first_sale, all_count, all_sold, top_ten
