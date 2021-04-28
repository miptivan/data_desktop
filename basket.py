import pandas as pd
import numpy as np
from apyori import apriori
import os


def bascket_analysis(ys):
    list_dir = os.listdir('analysis')
    if 'basket_table_' + '_'.join([str(y) for y in ys]) + '.csv' not in list_dir:
        dfs = []
        for y in ys:
            df = pd.read_csv(f'analysis/EtsySoldOrderItems{y}.csv')
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
            item_1 = res[i][2][0][0]
            item_2 = res[i][2][0][1]
            support = res[i][1]
            confidence = res[i][2][0][2]
            lift = res[i][2][0][3]
            res_df.loc[len(res_df)] = [item_1, item_2, support, confidence, lift]
        print(res_df)

bascket_analysis(range(2015, 2020))