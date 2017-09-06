from pandas import json


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

