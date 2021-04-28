import pandas as pd
import numpy as np
import os
from datetime import date


def abc(ys):
    list_dir = os.listdir('analysis')
    if 'ABC_table_' + '_'.join([str(y) for y in ys]) + '.csv' not in list_dir:
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
        
        all_items = all_items[['Item Name', 'Item Total']]
        all_items = all_items.groupby('Item Name')['Item Total'].sum()
        all_items = pd.DataFrame(data=np.array([all_items.index, all_items.values]).T, columns=['Item Name', 'Item Total'])

        summ = all_items['Item Total'].values.sum()
        all_items['total_percentage'] = all_items['Item Total'].values/summ
        all_items = all_items.sort_values(by='Item Total', ascending=False)

        all_items['cum_perc'] = np.cumsum(all_items['total_percentage'].values)

        def group(x):
            if x < 0.8:
                return 'A'
            elif x < 0.95:
                return 'B'
            else:
                return 'C'

        all_items['group'] = all_items['cum_perc'].apply(group)
        all_items.to_csv('analysis/ABC_table_' + '_'.join([str(y) for y in ys]) + '.csv')  # создали табличку ABC анализа
    return
