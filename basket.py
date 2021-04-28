import pandas as pd
import numpy as np
from apyori import apriori
import os


def bascket_info(ys, path):
    list_dir = os.listdir(path)
    if 'basket_table_' + '_'.join([str(y) for y in ys]) + '.csv' not in list_dir:
        dfs = []
        for y in ys:
            df = pd.read_csv(path + f'/EtsySoldOrderItems{y}.csv')
            dfs.append(df)

        Df_tr = dfs[0]
        for i in range(1, len(dfs)):
            Df_tr = Df_tr.append(dfs[i])
        
        Df_tr = Df_tr.groupby('Order ID')
        grps = Df_tr.groups

        trscs = []
        for gr in grps:
            trscs.append(list(Df_tr.get_group(gr)['Item Name'].values))
        
        res = list(apriori(trscs, min_support=0.003, min_confidence=0.05, min_lift=1, min_length=2))

        # распарсим немного результат
        res_df = pd.DataFrame(data=[], columns=['If this', 'Then this', 'Support', 'Confidence', 'Lift'])
        for i in range(len(res)):
            item_1 = ', '.join([s for s in res[i][2][0][0]])
            item_2 = ', '.join([s for s in res[i][2][0][1]])
            support = round(res[i][1], 4)
            confidence = round(res[i][2][0][2], 4)
            lift = round(res[i][2][0][3], 4)
            res_df.loc[len(res_df)] = [item_1, item_2, support, confidence, lift]
        res_df = res_df[res_df['Lift'] >= 2.0]
        res_df = res_df.sort_values(by='Lift', ascending=False)
        res_df.to_csv(path + '/basket_table_' + '_'.join([str(y) for y in ys]) + '.csv')
    return