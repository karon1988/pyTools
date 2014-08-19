import csv
import json

"""
Convert multiple JSONs(with the same structure) to CSV
input is a list of dict
output is a csv file
Args:
    in_json:list(dict):list of a dictionary
    out_file:str:filepath of output csv flie
"""

def json2csv(in_json, out_file):
    if not type_check(in_json):
        raise TypeError("The first parameters should be a dictionary or a \
                         list of dictionary") 

    headers = list()
    with open(out_file, "wb") as f:
        writer = csv.writer(f)
        for j in in_json:
            if not headers:
                headers = get_headers(j)
                writer.writerow(headers)
            row = list()
            for h in headers:
                try:
                    row.append(j[h])
                except KeyError:
                    row.append("")
            writer.writerow(row)



def get_headers(in_dict):
    tmp_headers = in_dict.keys()
    headers = list()
    for h in tmp_headers:
        headers.append(h)
    return headers


def type_check(in_json):
    if type(in_json) is not list:
        return False
    else:
        for e in in_json:
            if type(e) is not dict:
                return False
        return True
    
# TODO:add test code in main function
if __name__ == "__main__":
    pass
