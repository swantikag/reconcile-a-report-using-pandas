# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df["state"]=df["state"].str.lower
df["total"]=df["Jan"]+df["Feb"]+df["Mar"]
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()
df_final = df.append(sum_row, ignore_index=True)
# Code ends here


# --------------
import requests

# Code starts here
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1 = df1.loc[11:]
df1.columns = df1.iloc[0]
df1.drop(df.index[11], inplace = True)
df1["United States of America"]=df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)
print(df1)
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = df1.set_index('United States of America')['US'].to_dict()
print(mapping)
mapping.update(dict({'mississipi': 'MS', 'tenessee':'TN', 'nan':'nan'}))
df_final["abbr"] = df_final["state"].astype(str).apply(lambda x: mapping[x])
# Code ends here
# df1["United States of America"]=df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)


# --------------
# Code stars here
mississipi = df_final.loc[df_final["state"]=="mississipi"].replace(np.nan, "MS")
print(mississipi)
df_final.replace(df_final.iloc[6], mississipi, inplace=True)
tenesse = df_final.loc[df_final["state"]=="tenessee"].replace(np.nan, "TN")
print(tenesse)
df_final.replace(df_final.iloc[10], tenesse, inplace=True)
# # Code ends here


# --------------
# Code starts here
df_sub = df_final.groupby("abbr")[["Jan", "Feb", "Mar", "total"]].sum()
print(df_sub)
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))
print(formatted_df)
# Code ends here


# --------------
# Code starts here
sum_row = df_final[["Jan", "Feb", "Mar", "total"]].sum()
print(sum_row)
df_sub_sum = sum_row.transpose()
print(df_sub_sum)
df_sub_sum = df_sub_sum.map(lambda x: "${:,.0f}".format(x))
final_table = formatted_df.append(df_sub_sum, ignore_index=True)
print(final_table)
# Code ends here


# --------------
# Code starts here
df_sub['total']=df_sub[["Jan", "Feb", "Mar"]].sum()
df_sub['total'].plot.pie()
# Code ends here


