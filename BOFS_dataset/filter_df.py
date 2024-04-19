import pandas as pd


# list of active subscription statuses
OID=['CD46_0305C#4','CD46_0405C#8','CD46_0605C#6','CD46_1105C#6','CD46_1305C#3','CD46_1905C#2']
df=pd.read_csv("CD46_phys_oce_bottle.tab",sep='\t',skiprows=127,engine='python')
# filter rows based on list values
mask = df['Event'].isin(OID)
df_filter = df[mask]

df_filter.to_csv("CD46_phys_oce_bottle.tab.filtered",sep='\t',index=False)
