# -*- encoding: utf-8 -*-
import re
from bosonnlp import BosonNLP
import json


def boson_ner(nlp, s):
    result_p1 = ""
    result_p2 = ""
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("\r", "")
    s_p1 = s
    if len(s) > 5000:
        sub_index = s[0:4999].rindex("。")
        s_p1 = s[0:sub_index]
        result_p2 = boson_ner(nlp, s[sub_index:])
    result = nlp.ner(s_p1, sensitivity=3, segmented=False)[0]
    words = result["word"]
    entities = result["entity"]
    start = 0
    for entity in entities:
        if start == entity[0]:
            result_p1 = result_p1 + "".join(words[entity[0]:entity[1]]) + "/" + entity[2] + " "
        elif start < entity[0]:
            result_p1 = result_p1 + "".join(words[start:entity[0]]) + "/" + "not_entity" + " "
            result_p1 = result_p1 + "".join(words[entity[0]:entity[1]]) + "/" + entity[2] + " "
        start = entity[1]
    return result_p1 + " " + result_p2 if len(result_p2) >= 1 else result_p1

if __name__ == "__main__":

    # 注意：在测试时请更换为您的API token
    nlp = BosonNLP('Pf9PQqVF.15107.z0WLjI-dZeOu')

    with open("/Users/lsx/Desktop/命名实体识别/data.json/part-00000", "r") as input_file:
        lines = input_file.readlines()
        json_list = [json.loads(line) for line in lines]
        ner_result = [boson_ner(nlp, j["text"]) for j in json_list]
        with open("/Users/lsx/Desktop/命名实体识别/ner_result.txt", "w") as output_file:
            output_file.writelines("\n".join(ner_result))



