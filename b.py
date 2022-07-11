import pandas as pd

a = pd.read_csv('new_name.csv')
a['new_t'] = pd.Series(a['new_t'], dtype="string")
a['new_t1']=["0" + x.replace('.0','') if type(x)==type("abc") else 0 for x in a['new_t']]
a.to_csv("data1.csv",index=False)
# print(a['new_t'])