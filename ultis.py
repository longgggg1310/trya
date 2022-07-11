import pandas as pd
import json

def read_data(path):
    find_data = open(path, 'r', encoding="utf-8")
    Lines = find_data.readlines()
    list_column_key = ['fbid', 't','pname','gender','curr_town','zalo_used']
    pd.set_option('display.max_columns', None)
    df_data = pd.DataFrame(columns = list_column_key)
    for line in Lines[:20]:
        row_str = line.replace("\n", "")
        row_dict = json.loads(row_str)
        df_data = df_data.append(row_dict, ignore_index=True)
        # df1 = pd.DataFrame(columns = row_dict)
        # df_data = pd.DataFrame()

        # pd.concat([df_data,df1])
    df_data = df_data[list_column_key]
    return df_data

def write_data(df_data, path):
    df_data.to_csv(path, index = None, sep = '\t', mode = 'w' )