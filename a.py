import pandas as pd 
tsv_file='raw_data\part-01.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('new_name.csv',index=False)