import pandas as pd
import numpy as np

def main_info(ys):
    dfs = []
    for y in ys:
        exec(f'analys/df = pd.read_csv("EtsySoldOrderItems{y}.csv")')
        dfs.append(df)