import pandas as pd


def generate_tree(file_name, desc_file_name):
    df = pd.read_excel(file_name)
    desc_df = pd.read_excel(desc_file_name)
    desc_dict = dict()
    for index, row in desc_df.iterrows():
        desc_dict[row['Activity ID']] = row['Description']
    qq = list(df.iloc[3])
    d = dict()
    data_dict = dict()
    for index, w in enumerate(qq):
        data_dict[w] = index
        if index == 0 or index == 1:
            continue
        ll = w.split('.')
        get_data(d, index, ll, desc_dict)
    return d, data_dict, df


def get_data(work_dict, column, total_list, desc_dict, current_index=0, parent_name=""):
    if current_index >= len(total_list):
        return
    name = '{}.{}'.format(parent_name, total_list[current_index]) if parent_name else total_list[current_index]
    if not work_dict.get(name, None):
        work_dict[name] = {'column': column, 'description': desc_dict.get(name, ' '), 'children': {}}
    get_data(work_dict.get(name)['children'], column, total_list, desc_dict, current_index + 1, name)
