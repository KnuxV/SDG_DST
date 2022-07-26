import pandas as pd

from utils import filter_for_eu_countries

df_after = pd.read_pickle('data/dataframes/digital/digital_1975-2022.pkl')
df_tot = filter_for_eu_countries(df_after, how='add')
df_tot.to_pickle('data/dataframes/digital/digital_1975-2022.pkl')
