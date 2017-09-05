from pandas import json

import xmltodict
import pandas as pd


def transform_to_xmllist(lines, root_element):
    combine = False
    xml_str = ""
    xml_str_list = []
    for line in lines:
        if line.startswith("<" + root_element + ">"):
            combine = True
        if combine:
            xml_str += line
        if line.startswith("</" + root_element + ">"):
            combine = False
            xml_str_list.append(xml_str)
            xml_str = ""
    return xml_str_list


def parse_to_standard_dict(d):
    measurements = json.dumps(d, ensure_ascii=False)
    data_dict = json.loads(measurements)
    return data_dict


if __name__ == "__main__":
    path = "D:/搜狗实验室/SogouCS.WWW08.txt"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        xml_str_list = transform_to_xmllist(lines, "doc")
        xml_dict_list = list(map(xmltodict.parse, xml_str_list))
        xml_dict_list = list(map(parse_to_standard_dict, xml_dict_list))
        xml_df = pd.DataFrame(xml_dict_list)
        print(xml_df)
