import json
import codecs
import os

def get_all_key_in_data(path_input, get_from_line = 0):
    list_full_key = []
    with open(path_input, "r", encoding="utf-8") as file_data:
        Lines = file_data.readlines()
    for line in Lines[get_from_line:]:
        row_str = line.replace("\n", "")
        if r"\r" in row_str:
            row_str = row_str.replace(r"\r", "").replace("fbid", "t")
        row_dict = json.loads(row_str)
        for key in row_dict.keys():
            if key in list_full_key:
                pass
            else:
                list_full_key.append(key)                   
    return list_full_key

def dict_to_str(
    row_dict, 
    list_column_key = ["fbid", "t", "n", "gender", "fb_birthday", "fb_email", "a"],
):

    row_str = ""
    for key in list_column_key:
        try:
            row_str += str(row_dict[key]) + "\t"
        except:
            row_str += "\t"
    row_str = row_str[:-1] + "\n"
    return row_str

def convert_data(
    path_input, 
    path_output,
    list_column_key = ["fbid", "t", "n", "gender", "fb_birthday", "fb_email", "a"],
    get_from_line = 0,
):
    
    with open(path_input, "r", encoding="utf-8") as file_data:
        Lines = file_data.readlines()
    
    file_output = codecs.open(path_output, "w", "utf-8")
    
    row_str_write = ""
    for key in list_column_key:
        row_str_write = row_str_write + key +"\t"    
    row_str_write = row_str_write[:-1]+ "\n"
    file_output.write(row_str_write)    
    
    for line in Lines[get_from_line:]:
        row_str = line.replace("\n", "")
        if r"\r" in row_str:
            row_str = row_str.replace(r"\r","").replace("fbid","t")
        row_dict = json.loads(row_str)
        row_dict['n'] = row_dict['n'].replace('"', '')
        row_str_write = dict_to_str(row_dict = row_dict, 
                                    list_column_key = list_column_key)
        file_output.write(row_str_write)


if __name__ == "__main__":
    
    list_column_key = ["fbid", "t", "n", "gender", "fb_birthday", "fb_email", "a"]
    path_input_folder = "raw_data"
    path_output_folder = "preprocessed_data"
    First_path = True
    for input_file in os.listdir(path_input_folder):
        name_file = input_file[:-4]
        print(name_file)
        input_file_path = path_input_folder + "/" + name_file + ".sql"
        output_file_path = path_output_folder + "/" + name_file + ".tsv"
        
        if name_file == "part-01":
            get_from_line = 1
        else:
            get_from_line = 0

        print("input path: ", input_file_path)
        print("output path: ", output_file_path)
        convert_data(
            path_input = input_file_path, 
            path_output = output_file_path, 
            list_column_key = ["fbid", "t", "n", "gender", "fb_birthday", "fb_email", "a"],
            get_from_line = get_from_line
        )
