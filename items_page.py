import pandas as pd
import numpy as np
from datetime import date


def items_info(ys, path):
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

    abc = pd.read_csv(path + '/ABC_table_' + '_'.join([str(y) for y in ys]) + '.csv')
    all_items = pd.merge(all_items, abc, on='Item Name', how='left')
    all_sums = all_items.groupby('Item Name')[['Quantity', 'Item Total_x']].sum()
    all_sums = pd.DataFrame(data=np.array([all_sums.index, all_sums['Quantity'].values, all_sums['Item Total_x'].values]).T, columns=['Item Name', 'Quantity', 'Item Total'])
    all_items = all_items.groupby('Item Name')[['Price', 'group']].min()
    all_items = pd.DataFrame(data=np.array([all_items.index, all_items['Price'].values, all_items['group'].values]).T, columns=['Item Name', 'Price', 'Group'])
    all_items = pd.merge(all_sums, all_items, on='Item Name', how='left')
    

    active_items = pd.read_csv(path + '/EtsyListingsDownload.csv')
    active_items['Item Name'] = active_items['TITLE']
    del active_items['TITLE']
    active_names = list(active_items['Item Name'].values)
    active_items = pd.DataFrame(data=active_names, columns=['Item Name'])
    active_items = pd.merge(active_items, all_items, on='Item Name', how='left')

    def f(x):
        if x in active_names:
            return False
        else:
            return True

    disactive_items = all_items[all_items['Item Name'].apply(f)]
    print(len(all_items), len(active_items), len(disactive_items))
    return all_items, active_items, disactive_items